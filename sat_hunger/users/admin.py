from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegisterForm
from .models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form =  UserRegisterForm
    
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Details',{
                'fields':(
                    'locality',
                    'pincode',
                    'city',
                    'state'
                )
            }
        )
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)