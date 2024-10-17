from django.contrib import admin
from django.urls import path,include 
from . import views

urlpatterns = [
    path('home', views.home , name="home"),
    path('service', views.service , name="service"),
    # path('', include('lumsdale.urls')),
    # path('', include('loginapp.urls')),

]
