from django.shortcuts import HttpResponse,render
from django.contrib.auth.decorators import login_required
import requests
import json

# Create your views here.
@login_required(login_url='login')
def home(request):
    url = "https://api.spoonacular.com/food/jokes/random?apiKey=c4a6aef8abe243de923c9cc7f7a769d2"
    res = requests.get(url)
    food_joke = json.loads(res.content.decode('utf-8'))

    url1 = "https://api.spoonacular.com/food/trivia/random?apiKey=c4a6aef8abe243de923c9cc7f7a769d2"
    res1 = requests.get(url1)
    trivia = json.loads(res1.content.decode('utf-8'))

    context={"food_joke":food_joke,"food_trivia":trivia}
    return render(request,'main_app/index.html',context)

def sati(request):
    return render(request, 'main_app/sati.html')