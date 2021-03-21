from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sati, name='sati'),
    path('home/',views.home,name="home"),
]