from .models import *
from django import forms

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = AddedRecipe
        exclude = ("user", "image", "approval")


class AddRecipeImageForm(forms.Form):
    image = forms.ImageField()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["user", "recipe", "text","rating"]