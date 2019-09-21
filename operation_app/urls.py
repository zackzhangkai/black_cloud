from django.urls import path
from operation_app import views


urlpatterns = [
    path('operation_board/', views.operation_board, name='operation_board'),
    path('upload_file/', views.handle_uploading_file, name='upload_file'),
    path('view_file/', views.view_file, name='view_file'),
    path('download_file/', views.download_file, name='download_file'),
    path('delete_file_from_user_space/', views.delete_file_from_user_space, name='delete_file_from_user_space'),
    path('share_space/', views.share_space, name='share_space'),
    path('share_file_to_another/', views.share_file_to_another, name='share_file_to_another'),
    path('delete_this_sharing/', views.delete_this_sharing, name='delete_this_sharing'),
]
