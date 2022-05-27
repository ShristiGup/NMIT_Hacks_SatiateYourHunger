from django.urls import path
from . import views

urlpatterns = [
    path('donate/',views.donate,name="donate"),

]