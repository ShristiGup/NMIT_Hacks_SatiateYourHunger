from django.shortcuts import render
import requests
import json

# Create your views here.
def recipe(request):
    return render(request,'recipes/find_recipe.html')

list3 = []
food_cat = ""
btn_color = ""

def show_recipe(request):
    globals()['list3'] = []
    ingre = request.POST.get('ingredients')
    globals()['food_cat'] = request.POST.get('food_cat')
    prep_time = request.POST.get('prep_time')
    # cooking_time = 0

    url1 = "https://api.spoonacular.com/recipes/findByIngredients?ingredients="+str(ingre)+"&number=15&ranking=1&apiKey=0c360133fcc5485aa89304473473a0bd"
    response = requests.get(url1)
    data = json.loads(response.content.decode('utf-8'))
    
    recipe_ids = []
    for i in data:
        recipe_ids.append(i['id'])
    
    recipe_info_list = []
    url2 = "https://api.spoonacular.com/recipes/informationBulk?ids="+str(recipe_ids)[1:-1]+"&includeNutrition=true&apiKey=0c360133fcc5485aa89304473473a0bd"
    url2 = url2.replace(" ","")
    resp = requests.get(url2)
    recipe_info_list = json.loads(resp.content.decode('utf-8'))
    
    list1=[]
    list2=[]
    
    for i in recipe_info_list:
        if food_cat=="Veg" and str(i['vegetarian']) == "True":
            list1.append(i)
            globals()['btn_color'] = "success"
        elif food_cat=="Non-Veg" and str(i['vegetarian']) == "False":
            list1.append(i)
            globals()['btn_color'] = "danger"
    

    for i in list1:
        if prep_time=="Starving" and int(i['readyInMinutes'])<=15:
            list2.append(i)
        elif prep_time=="Pretty hungry" and int(i['readyInMinutes'])<=25:
            list2.append(i)
        elif prep_time=="Satisfied":
            list2.append(i)

    for i in list2:
        for j in data:
            if i['id'] == j['id']:
                i.update(j)
                globals()['list3'].append(i)

    if len(data)!=0 and len(list1)!=0 and len(list2)!=0:
        context={'recipe_items':list3,'food_cat':food_cat,'btn_color':btn_color}
        return render(request,'recipes/show_recipes.html',context)
    else:
        return render(request,'recipes/show_recipes.html')