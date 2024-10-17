from django.contrib import admin
from django.urls import path,include 
from . import views

urlpatterns = [
    path('game', views.game , name='game'),
    path('car', views.car , name='car'),
    path('product', views.product , name='product')
    # path('', include('lumsdale.urls')),
    # path('', include('loginapp.urls')),
    # path('', include('success.urls')),


]
