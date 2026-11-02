from django.urls import path
from . import views

urlpatterns = [
    path('', views.initialPage, name='initialPage_Name'),
    path('admin/', views.adminPage, name='adminPage_Name'),
    path('principal/', views.initialPage, name='mainPage_Name'),
    path('responder/<int:post_id>/', views.send_reply, name='sendReply_Name'),
    path('posted/', views.sendPost, name='sendPost_Name')
]
