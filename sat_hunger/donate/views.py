from django.shortcuts import render
from .models import *
from .forms import *
from django.utils import timezone

def donate(request):
    return render(request,'donate/donate.html')

def recorded(request):
    form = DonationForm(request.POST)
    if form.is_valid():
        donate = form.save(commit=True)
        donate.user = request.user
        donate.save()
        return render(request,'donate/recorded.html', {'donation': True})
    return render(request,'donate/recorded.html', {'donation': False})

def find_food(request):
    obj = FoodDonate.objects.all()
    return render(request,'donate/find_food.html', context={'donations': obj, "current_date": timezone.now()})

def request_food(request):
    data = {
        "user": request.user,
        "food": FoodDonate.objects.get(id=request.POST.get("food_id"))
    }
    form = RequestFoodForm(data)
    if form.is_valid():
        form.save()
        return render(request,'donate/requested.html', {'requested': True})
    return render(request,'donate/requested.html', {'requested': False})
    