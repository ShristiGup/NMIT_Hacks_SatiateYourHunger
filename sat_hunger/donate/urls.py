from django.urls import path
from . import views

urlpatterns = [
    path('donate/',views.donate,name="donate"),
    path('recorded/',views.recorded,name="donation_recorded"),
    path('find_food/',views.find_food,name="find_food"),
    path('request_food/',views.request_food,name="request_food"),

]