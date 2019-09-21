from django.urls import path
from hotlist_app import views


urlpatterns = [
    # path('login/', views.login, name='show_login_page'),
    path('show_top_list/', views.show_top_list, name='show_top_list'),

]

