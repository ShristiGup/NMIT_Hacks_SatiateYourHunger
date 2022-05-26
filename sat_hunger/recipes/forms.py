from .models import *
from django import forms

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = AddedRecipe
        fields = ['ingredients','steps', 'readyInMinutes', 'food_cat']