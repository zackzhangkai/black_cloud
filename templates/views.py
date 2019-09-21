from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from community_app.models import Topic, Comment, StarUser, UserScore

# Create your views here.


@login_required
def show_my_info(request):
    """展示当前用户信息"""
    user_id = request.user.id
    print('im-user')
    print(user_id)
    submit_cnt = len(Topic.objects.filter(user__pk=user_id))
    comment_cnt = len(Comment.objects.filter(user__pk=user_id))

    return render(request, 'u_center_app/user_info.html',
                  context={
                      'submit_cnt': submit_cnt,
                      'comment_cnt': comment_cnt,
                           })


@login_required
def show_my_success(request):
    """展示当前用户成就"""

    return render(request, 'u_center_app/user_success.html')





