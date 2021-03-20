from django.urls import path
from . import views

urlpatterns = [
    path('find-recipes-by-ingredients/',views.recipe,name="find_recipe"),
]
