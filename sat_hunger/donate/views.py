from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.utils import timezone
from django.db.models import Q


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
    obj = FoodDonate.objects.filter(~Q(user=request.user)).order_by('-timestamp')
    return render(request,'donate/find_food.html', context={'donations': obj})


def request_food(request):
    data = {
        "user": request.user,
        "food": FoodDonate.objects.get(id=request.POST.get("food_id")),
        "no_of_people": request.POST.get("no_of_people")
    }
    form = RequestFoodForm(data)
    if form.is_valid():
        form.save()
        return render(request,'donate/requested.html', {'requested': True})
    return render(request,'donate/requested.html', {'requested': False})


def your_donations (request):
    obj = FoodDonate.objects.filter(user=request.user).order_by('-timestamp')
    return render(request,'donate/your_donations.html', {'your_donations': obj})


def your_requests(request):
    obj = RequestFood.objects.filter(user=request.user).order_by('-timestamp')
    return render(request,'donate/your_requests.html', {'food_requests': obj})
    

def donation_requests(request, id):
    food = FoodDonate.objects.get(pk=id)
    request_food = RequestFood.objects.filter(food=food)
    return render(request,'donate/donation_requests.html', {'donation_requests': request_food, "food_id": id})


def approve_request (request, id):
    obj = RequestFood.objects.get(pk=id)
    obj.approval = request.GET.get('approval')
    obj.save()
    if obj.approval == 'approved':
        f_obj = FoodDonate.objects.get(id=request.GET.get('food_id'))
        f_obj.no_of_people -= obj.no_of_people
        f_obj.save()
    return redirect('donation_requests', id=request.GET.get('food_id'))
