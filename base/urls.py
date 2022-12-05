from django.urls import path
from . import views

urlpatterns = [

    path('', views.lobby),
    path('room/', views.room),
    path('getToken/', views.getToken),
    path('create_member/', views.createUser),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),

]
