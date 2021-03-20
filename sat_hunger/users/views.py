from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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