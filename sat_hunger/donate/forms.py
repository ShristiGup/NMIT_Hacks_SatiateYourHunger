from .models import *
from django import forms

class DonationForm(forms.ModelForm):
    class Meta:
        model = FoodDonate
        exclude = ("user", 'timestamp')

class RequestFoodForm(forms.ModelForm):
    class Meta:
        model = RequestFood
        fields = ("user", "food", "no_of_people")
