from django.urls import path
from . import views

urlpatterns = [
    path('find-recipes-by-ingredients/',views.recipe,name="find_recipe"),
    path('show-recipes/',views.show_recipe,name="show_recipe"),
    path('recipe-detail/<int:id>/',views.recipe_detail,name="recipe_detail")
]
