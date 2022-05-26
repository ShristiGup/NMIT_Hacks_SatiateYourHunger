from django.contrib import admin
from .models import *

# Register your models here
class AddedRecipeAdmin(admin.ModelAdmin):
    list_filter = ('timestamp', 'approval', 'food_cat')
    list_display = ("title", "user", "food_cat")

admin.site.register(RecentSearches)
admin.site.register(AddedRecipe, AddedRecipeAdmin)
admin.site.register(Review)

