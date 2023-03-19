from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.userLogin,name='login'),
    path('register/',views.userRegister,name='register'),
    path('logout/',views.userLogout,name='logout'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('updateprofile/<str:pk>/',views.updateProfile,name='updateprofile'),
    path('chatusers',views.chatUsers,name='chatusers'),
    

] 