from django.shortcuts import HttpResponse,render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return HttpResponse('This is some text')