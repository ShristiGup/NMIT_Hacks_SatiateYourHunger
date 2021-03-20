from django.shortcuts import render
import requests
import json

# Create your views here.
def recipe(request):
    return render(request,'recipes/find_recipe.html')

