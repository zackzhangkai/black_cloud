from django.urls import path
from event_center_app import views


urlpatterns = [
    # path('login/', views.login, name='show_login_page'),
    path('query_event/', views.query_event, name='query_event'),
    path('display_event/', views.display_event, name='display_event'),

]

