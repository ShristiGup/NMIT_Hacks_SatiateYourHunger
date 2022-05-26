from django.contrib import admin
from .models import *

# Register your models here

admin.site.register(RecentSearches)
admin.site.register(AddedRecipe)
admin.site.register(Review)

