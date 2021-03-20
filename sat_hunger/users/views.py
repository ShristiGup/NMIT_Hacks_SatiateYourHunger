from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from recipes.models import *

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data['username']
                messages.success(request,'Account successfully created for '+ user+'!')
                return redirect("login")
        else:
            form = UserRegisterForm()
        context = {"form":form}
        return render(request,"users/register.html",context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            usrnme = request.POST.get('username')
            pswd = request.POST.get('password')
            user = authenticate(request,username=usrnme,password=pswd)
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                messages.info(request,'Either username or password is incorrect!')

        return render(request,"users/login.html")

def logoutUser(request):
    logout(request)
    return redirect("login")

@login_required
def profile(request):
    if request.method=="POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your account info has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        recent_searches = RecentSearches.objects.filter(user=request.user).order_by('-id')[:5]
        if recent_searches:
            context = { 'u_form':u_form,
                        'p_form':p_form,
                        'recent_searches':recent_searches}
        else:
            context = { 'u_form':u_form,
                        'p_form':p_form,}
    return render(request,'users/profile.html',context)