from django.shortcuts import render


def donate(request):
    return render(request,'donate/donate.html')

# Create your views here.
