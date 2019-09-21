from django.urls import path
from community_app import views


urlpatterns = [
    #path('login/', views.login, name='show_login_page'),
    path('show_topics/', views.show_topics, name='show_topics'),
    path('comments/', views.comments, name='comments'),
    path('view_this_topic/', views.view_this_topic, name='view_this_topic'),
    path('star_this_topic/', views.star_this_topic, name='star_this_topic'),

]

