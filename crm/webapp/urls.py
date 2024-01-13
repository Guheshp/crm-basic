from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home, name=''),
    path('register', views.Register, name='my-register'),
    path('login', views.Login, name='my-login'),
    path('logout', views.Logout, name='my-logout'),
    path('dashboard', views.Dashboard, name='my-dashboard'),
    path('createrecord', views.CreateRecord, name='my-createrecord'),
    

]