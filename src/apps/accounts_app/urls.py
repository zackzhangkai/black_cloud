from django.urls import path
from apps.accounts_app import views


urlpatterns = [
    path('login/', views.login, name='show_login_page'),
    path('check_user/', views.check_user, name='check_user'),
    path('register/', views.register, name='show_register_page'),
    path('if_username_existed/', views.if_username_existed, name='if_username_existed'),
    path('new_account/', views.new_account, name='new_account'),
    path('logout/', views.logout, name='logout'),
]

