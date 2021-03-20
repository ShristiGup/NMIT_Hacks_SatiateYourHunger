from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['username','email','locality','pincode','city','state','password1','password2']
