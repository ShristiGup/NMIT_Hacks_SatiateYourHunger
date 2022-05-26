from django.shortcuts import render,redirect
from .models import *
import requests
import json
from .forms import *
from django.core import serializers

# Create your views here.

def recipe(request):
    return render(request,'recipes/find_recipe.html')

list3 = []
food_cat = ""
btn_color = ""
ingre = ""

def addRecipe(request):
    return render(request,'recipes/add_recipe.html')

def show_recipe(request):
    globals()['list3'] = []
    globals()['btn_color'] = ""
    globals()['ingre'] = request.POST.get('ingredients')
    globals()['food_cat'] = request.POST.get('food_cat')
    prep_time = request.POST.get('prep_time')

    
    if prep_time == "Starving":
        return redirect("https://www.zomato.com/ncr")

    context = {}
    try:
        url1 = "https://api.spoonacular.com/recipes/findByIngredients?ingredients="+str(ingre)+"&number=15&ranking=1&apiKey=c4a6aef8abe243de923c9cc7f7a769d2"
        response = requests.get(url1)
        if response.status_code>=200 and response.status_code<400:
            data = json.loads(response.content.decode('utf-8'))
            recipe_ids = []
            for i in data:
                recipe_ids.append(i['id'])
            
            recipe_info_list = []
            url2 = "https://api.spoonacular.com/recipes/informationBulk?ids="+str(recipe_ids)[1:-1]+"&includeNutrition=true&apiKey=c4a6aef8abe243de923c9cc7f7a769d2"
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
                if prep_time=="Pretty hungry" and int(i['readyInMinutes'])<=25:
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
                r_obj = RecentSearches(user=request.user,ingredients=str(ingre),food_cat=food_cat,hunger_level=prep_time)
                r_obj.save()
        
        user_recipes = []
        user_added_recipe = AddedRecipe.objects.filter(ingredients__contains=ingre, food_cat=food_cat)
        for recipe in user_added_recipe:
            user_recipes.append(json.loads(serializers.serialize('json', [ recipe, ]))[0])
        context['user_recipes'] = user_recipes
        return render(request,'recipes/show_recipes.html', context)

    except Exception as e:
        return render(request,'recipes/show_recipes.html')

def recipe_detail(request,id):
    recipe_item = ""
    cal = 0
    protein = 0
    carbs = 0
    fats = 0
    cholestrol = 0
    unit_c = ""
    unit_f = ""
    unit_p = ""
    unit_ch = ""
    unit_ca = ""
    for i in list3:
        if i['id'] == id:
            recipe_item = i
    nutrition = recipe_item['nutrition']['nutrients']
    for i in nutrition:
        if i['name']=="Calories":
            cal = round(int(i['amount']))
            unit_c = i['unit']
        elif i['name']=="Fat":
            fats = round(int(i['amount']))
            unit_f = i['unit']
        elif i['name']=="Carbohydrates":
            carbs = round(int(i['amount']))
            unit_ca = i['unit']
        elif i['name']=="Protein":
            protein = round(int(i['amount']))
            unit_p = i['unit']
        elif i['name']=="Cholesterol":
            cholestrol = round(int(i['amount']))
            unit_ch = i['unit']
    # missed_ingre_count = int(recipe_item['missedIngredientCount'])
    # used_ingre_count = int(recipe_item['usedIngredientCount'])
    missed_ingre = recipe_item['missedIngredients']
    used_ingre = recipe_item['usedIngredients']
    unused_ingre = recipe_item['unusedIngredients']
    # m_ing = 
    # for i in missed_ingre:


    url3 = "https://api.spoonacular.com/recipes/"+str(id)+"/analyzedInstructions?apiKey=9c71df05d86640df9865c5eb71775086"
    response = requests.get(url3)
    d = json.loads(response.content.decode('utf-8'))
    if len(d):
        method1 = d[0]
        steps = method1['steps']
    else:
        method1 = {}
        steps = []
    
    url4 = "https://api.spoonacular.com/food/videos/search?query="+str(recipe_item['title'])+"&number=3&apiKey=9c71df05d86640df9865c5eb71775086"
    response = requests.get(url4)
    videos = json.loads(response.content.decode('utf-8'))
    try:
        vd = videos['videos']
        if len(vd)!=0:
            context={'recipe_item':recipe_item,'food_cat':food_cat,'btn_color':btn_color,'fats':fats,'cal':cal,'protein':protein,'carbs':carbs,'cholestrol':cholestrol,'unit_c':unit_c,'unit_f':unit_f,'unit_p':unit_p,'unit_ch':unit_ch,'unit_ca':unit_ca,'steps':steps,'vd':vd}
        else:
            context={'recipe_item':recipe_item,'food_cat':food_cat,'btn_color':btn_color,'fats':fats,'cal':cal,'protein':protein,'carbs':carbs,'cholestrol':cholestrol,'unit_c':unit_c,'unit_f':unit_f,'unit_p':unit_p,'unit_ch':unit_ch,'unit_ca':unit_ca,'steps':steps}
    except:
        context={'recipe_item':recipe_item,'food_cat':food_cat,'btn_color':btn_color,'fats':fats,'cal':cal,'protein':protein,'carbs':carbs,'cholestrol':cholestrol,'unit_c':unit_c,'unit_f':unit_f,'unit_p':unit_p,'unit_ch':unit_ch,'unit_ca':unit_ca,'steps':steps}

    return render(request,'recipes/recipe_detail.html',context)

def exp_recipe(request):
    ex_rec = request.POST.get('recpe')
    url = "https://api.spoonacular.com/recipes/complexSearch?query="+str(ex_rec)+"&number=1&apiKey=9c71df05d86640df9865c5eb71775086"
    res = requests.get(url)
    result = json.loads(res.content.decode('utf-8'))

    a = result['results']
    b = a[0]

    url = "https://api.spoonacular.com/recipes/"+str(b['id'])+"/ingredientWidget?apiKey=9c71df05d86640df9865c5eb71775086"
    res1 = requests.get(url)
    result1 = json.loads(res.content.decode('utf-8'))

    return render(request,'recipes/explore_recipe.html')

def save_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'recipes/recipie_added.html', context={"recipe_items": True})

    else:
        return render(request,'recipes/recipie_added.html', context={"recipe_items": False})

