import os.path
import logging
import datetime
from django.http import FileResponse
from netstore.settings import MEDIA_ROOT
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from apps.operation_app.utils.processor import get_hashed_name
from apps.operation_app.models import FilesRecorder, SharingRecorder

# Create your views here.


@login_required
def operation_board(request):
    """返回用户操作页面,并显示当前用户已上传的所有文件"""
    uid = request.user.id
    current_page = 1 if not request.GET.get('current_page') else request.GET.get('current_page')
    holder = FilesRecorder.objects.filter(was_in_trashbin=False)
    paginator = Paginator(object_list=holder, per_page=10)
    try:
        page = paginator.page(current_page)
    except EmptyPage as e:
        # record meaningless request
        logging.info(f"uid-{uid} try to access page-{current_page}")
        return HttpResponse('您访问了不存在的页面！')
    return render(request, 'user_operations_app/operation_board.html',
                  context={'page': page})


@login_required
def handle_uploading_file(request):
    """处理上传的文件"""
    current_user = request.user
    upload_file = request.FILES.get('upload_file')
    content_type = upload_file.__dict__.get('content_type')
    file_type = content_type.split('/')[-1]
    filename = upload_file.__dict__.get('_name')

    # get the unique hashed filename
    hashed_name = get_hashed_name(upload_file)

    # modify the storage name to hashed filename
    upload_file.__dict__['_name'] = hashed_name
    size = upload_file.__dict__.get('size')

    # file is measured in byte
    # if the size larger than 1mb, use the mb
    # if the size smaller than 1000kb, use the kb
    size = str(round(size/1000, 2))+'KB' if size < 1000000 else str(round(size/1000000, 2)) + 'MB'

    # check if duplicated
    if FilesRecorder.objects.filter(file_path=hashed_name):
        # the key for not saving the existed file again
        logging.info(f"uploading-existed-file: {hashed_name}")
        upload_file = str(upload_file)
    # print(upload_file, type(upload_file), '+++++++')
    # insert into database
    FilesRecorder.objects.create(user=current_user, file_path=upload_file,
                                 content_type=content_type, file_type=file_type,
                                 size=size, file_name=filename, hashed_name=hashed_name)
    return HttpResponse('upload-success')


@login_required
def download_file(request):
    """用户下载文件"""
    file_name = request.GET.get('file_name')
    hashed_name = request.GET.get('hashed_name')
    processed_filename = file_name.encode("utf-8").decode("ISO-8859-1")
    filepath = os.path.join(MEDIA_ROOT, hashed_name)
    response = FileResponse(open(filepath, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    # it's necessary to process the filename to cope with the chinese filename
    response['Content-Disposition'] = f'attachment;filename="{processed_filename}"'
    return response


@login_required
def delete_file_from_user_space(request):
    """将要删除的文件加删除状态标记，并附上删除时间"""
    file_id = request.GET.get('file_id')
    on_delete_file = FilesRecorder.objects.get(id=file_id)
    # enable the abandoned flag
    on_delete_file.was_in_trashbin = True
    on_delete_file.deleting_time = datetime.datetime.now()
    on_delete_file.save()
    return redirect('operation_app:operation_board')


@login_required
def share_space(request):
    """显示分享空间页面"""
    user_id = request.user.id
    current_page = 1 if not request.GET.get('current_page') else request.GET.get('current_page')
    share_files = SharingRecorder.objects.filter(receiver=user_id,
                                                 expiry__gt=datetime.datetime.now())
    paginator = Paginator(object_list=share_files, per_page=10)

    # user can modify the 'current_page' in the URL
    # this try-except is designed for user's illegal input
    try:
        page = paginator.page(current_page)
    except EmptyPage as e:
        return HttpResponse('您访问了不存在的页面！')
    return render(request, 'user_operations_app/share_space.html',
                  context={'page': page})


@login_required
def share_file_to_another(request):
    """分享文件给另一个用户"""
    receiver_username = request.GET.get('receiver_username')
    file_hashed_name = request.GET.get('hashed_name')
    is_private = request.GET.get('is_private')
    expiry = request.GET.get('expiry')

    file = FilesRecorder.objects.filter(hashed_name=file_hashed_name).first()
    owner = User.objects.get(id=file.user.id)
    sharer = request.user
    if receiver_username == request.user.username:
        return HttpResponse('share-to-yourself')
    try:
        receiver = User.objects.get(username=receiver_username)
    except User.DoesNotExist:
        return HttpResponse('wrong-username')
    else:
        # username makes sense, create one record
        SharingRecorder.objects.create(owner=owner, sharer=sharer, receiver=receiver, file=file,
                                       is_private_sharing=is_private, expiry=expiry)
    return HttpResponse('sharing-success')


@login_required
def delete_this_sharing(request):
    """从分享记录表中删除一条分享记录,并记录删除操作的时间"""
    record_id = request.GET.get('record_id')
    on_delete = SharingRecorder.objects.get(id=record_id)
    # fix the record's status and append the timestamp
    on_delete.was_deleted = True
    on_delete.deleted_time = datetime.datetime.now()
    on_delete.save()
    return HttpResponse('delete-success')




