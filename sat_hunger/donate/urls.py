from django.urls import path
from . import views

urlpatterns = [
    path('donate/',views.donate,name="donate"),
    path('recorded/',views.recorded,name="donation_recorded"),
    path('find-food/',views.find_food,name="find_food"),
    path('request-food/',views.request_food,name="request_food"),
    path('donation-requests/<int:id>/',views.donation_requests,name="donation_requests"),
    path('your-donations/',views.your_donations,name="your_donations"),
    path('your-requests/',views.your_requests,name="your_requests"),
    path('approve-request/<int:id>/',views.approve_request,name="approve_request"),

]