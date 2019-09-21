from django.urls import path
from community_app import views


urlpatterns = [
    #path('login/', views.login, name='show_login_page'),
    path('show_topics/', views.show_topics, name='show_topics'),
    path('show_comments/', views.show_comments, name='show_comments'),

]

