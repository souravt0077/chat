from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('createroom/',views.createRoom,name='createroom'),
    path('available_rooms/',views.available_rooms,name='available_rooms'),
    path('room/<str:pk>/',views.room,name='room'),
    path('room_password/<str:pk>/',views.room_password,name='room_password'),
    path('updateroom/<str:pk>/',views.updateRoom,name='updateroom'),
    path('deleteroom/<str:pk>/',views.deleteRoom,name='deleteroom'),
    path('deletemessage/<str:pk>/',views.deleteMessage,name='deletemessage'),
    path('ask',views.askDoubts,name='ask'),
   
    
]
