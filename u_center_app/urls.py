from django.urls import path
from u_center_app import views

urlpatterns = [
    # path('operation_board/', views.operation_board, name='operation_board'),
    path('u_center_board/', views.show_my_info, name='u_center_board'),
    path('u_success_board/', views.show_my_success, name='u_success_board'),

]
