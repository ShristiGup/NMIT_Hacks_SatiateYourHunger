from django.contrib import admin
from .models import *

class RequestFoodAdmin(admin.ModelAdmin):
    list_display = ("user", "food")


admin.site.register(FoodDonate)
admin.site.register(RequestFood, RequestFoodAdmin)