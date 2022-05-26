from django.urls import path
from . import views

urlpatterns = [
    path('find-recipes-by-ingredients/',views.recipe,name="find_recipe"),
    path('add-recipe/',views.addRecipe,name="add_recipe"),
    path('explore-recipes-by-ingredients/',views.exp_recipe,name="explore_recipe"),
    path('show-recipes/',views.show_recipe,name="show_recipe"),
    path('save-recipe/',views.save_recipe,name="save_recipe"),
    path('recipe-detail/<int:id>/',views.recipe_detail,name="recipe_detail")
]
