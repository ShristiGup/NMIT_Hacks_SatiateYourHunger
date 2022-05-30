from django.shortcuts import HttpResponse,render
from django.contrib.auth.decorators import login_required
import requests
import json

# Create your views here.
@login_required(login_url='login')
def home(request):
    key = "2cfad58e575a4eeb969152c42a36b4b7"
    url = "https://api.spoonacular.com/food/jokes/random?apiKey="+key
    res = requests.get(url)
    food_joke = json.loads(res.content.decode('utf-8'))

    url1 = "https://api.spoonacular.com/food/trivia/random?apiKey="+key
    res1 = requests.get(url1)
    trivia = json.loads(res1.content.decode('utf-8'))

    context={"food_joke":food_joke,"food_trivia":trivia}
    return render(request,'main_app/index.html',context)

def sati(request):
    return render(request, 'main_app/sati.html')