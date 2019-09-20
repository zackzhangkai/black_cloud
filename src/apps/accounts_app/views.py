import logging
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse

# Create your views here.


def login(request):
    """显示登录页面"""
    return render(request, 'accounts_app/login.html')

def check_user(request):
    """检查用户名和密码是否正确"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request=request, user=user)
        logging.info(f'{username} log in')
        return HttpResponse('right-user')
    else:
        return HttpResponse('wrong-user')


def logout(request):
    """登出用户"""
    auth.logout(request)
    return render(request, 'accounts_app/logout.html')


def register(request):
    """显示注册页面"""
    return render(request, 'accounts_app/register.html')


def new_account(request):
    """在用户数据库中创建一个新用户"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    logging.info(f"new account: {username}, {email}")
    User.objects.create_user(username=username, password=password, email=email)
    return render(request, 'accounts_app/register_success.html')


def if_username_existed(request):
    """检查数据库中是否已存在这个用户名"""
    username = request.GET.get('username')
    if not User.objects.filter(username=username):
        return HttpResponse('not-existed')
    else:
        return HttpResponse('existed')



