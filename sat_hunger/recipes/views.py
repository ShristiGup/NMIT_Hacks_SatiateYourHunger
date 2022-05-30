from django.shortcuts import render,redirect
from .models import *
import requests
import json
from .forms import *
from django.core import serializers

# Create your views here.
list3 = []
food_cat = ""
btn_color = ""
ingre = ""
user_recipes = []
key = "4bd30dcb0062410aa39143d2cdc4bfd9"

def recipe(request):
    return render(request,'recipes/find_recipe.html')

def addRecipe(request):
    form = AddRecipeImageForm()
    return render(request,'recipes/add_recipe.html', {"form": form})

def show_recipe(request):
    globals()['list3'] = []
    globals()['btn_color'] = ""
    globals()['ingre'] = request.POST.get('ingredients')
    globals()['food_cat'] = request.POST.get('food_cat')
    prep_time = request.POST.get('prep_time')

    
    # if prep_time == "Starving":
    #     return redirect("https://www.zomato.com/ncr")

    context = {}
    try:
        url1 = "https://api.spoonacular.com/recipes/findByIngredients?ingredients="+str(ingre)+"&number=15&ranking=1&apiKey="+key
        response = requests.get(url1)
        if response.status_code>=200 and response.status_code<400:
            data = json.loads(response.content.decode('utf-8'))
            recipe_ids = []
            for i in data:
                recipe_ids.append(i['id'])
            
            recipe_info_list = []
            url2 = "https://api.spoonacular.com/recipes/informationBulk?ids="+str(recipe_ids)[1:-1]+"&includeNutrition=true&apiKey="+key
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
                if prep_time=="Starving" and int(i['readyInMinutes'])<=25:
                    list2.append(i)
                elif prep_time=="Pretty hungry" and int(i['readyInMinutes'])<=35:
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
        
        user_recipes = []
        for ing in ingre.split(','):
            ing = ing.lower()
            user_added_recipe = AddedRecipe.objects.filter(ingredients__contains=ing, food_cat=food_cat, approval='approved')
            print(user_added_recipe)
            for recipe in user_added_recipe:
                if set(ingre.split(',')) <= set(recipe.ingredients.split(',')) and recipe not in user_recipes:
                    user_recipes.append(recipe)
        context['user_recipes'] = user_recipes
        r_obj = RecentSearches(user=request.user,ingredients=str(ingre),food_cat=food_cat,hunger_level=prep_time)
        r_obj.save()
        return render(request,'recipes/show_recipes.html', context)

    except Exception as e:
        return render(request,'recipes/show_recipes.html')

def recipe_detail(request,id):
    if request.method == 'POST':
        user = request.user
        text = request.POST.get('text')
        rating = int(request.POST.get('rating'))
        recipe = AddedRecipe.objects.get(id=request.POST.get('recipe_id'))
        data = {
            'user': user,
            'text': text,
            'recipe': recipe,
            'rating': rating
        }
        form = ReviewForm(data)
        if form.is_valid():
            form.save()
        return redirect(request.path_info + '?recipe_type=0')


    
    if request.GET.get('recipe_type') == '0':
        obj = AddedRecipe.objects.get(id=id)
        reviews = []
        review_obj = Review.objects.filter(recipe=id)[::-1][:5]
        
        count = 0
        for review in review_obj:
            robj = {}
            robj['user'] = review.user
            robj['text'] = review.text
            robj['rating'] = review.rating
            reviews.append(robj)
        context={'recipe_item':obj,'food_cat':obj.food_cat,'btn_color':'green', 'steps':[obj.steps], 'vd': [obj], 'reviews': reviews}
        return render(request,'recipes/recipe_detail.html',context)

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
    
    missed_ingre = recipe_item['missedIngredients']
    m_ing = []
    for i in missed_ingre:
        m_ing.append(i['name'])
    other_ingre = str(",".join(m_ing)).title()

    url3 = "https://api.spoonacular.com/recipes/"+str(id)+"/analyzedInstructions?apiKey="+key
    response = requests.get(url3)
    d = json.loads(response.content.decode('utf-8'))
    if len(d):
        method1 = d[0]
        steps = method1['steps']
    else:
        method1 = {}
        steps = []
    
    url4 = "https://api.spoonacular.com/food/videos/search?query="+str(recipe_item['title'])+"&number=3&apiKey="+key
    response = requests.get(url4)
    videos = json.loads(response.content.decode('utf-8'))
    try:
        vd = videos['videos']
        if len(vd)!=0:
            context={'recipe_item':recipe_item,'other_ingre':other_ingre,'food_cat':food_cat,'btn_color':btn_color,'fats':fats,'cal':cal,'protein':protein,'carbs':carbs,'cholestrol':cholestrol,'unit_c':unit_c,'unit_f':unit_f,'unit_p':unit_p,'unit_ch':unit_ch,'unit_ca':unit_ca,'steps':steps,'vd':vd}
        else:
            context={'recipe_item':recipe_item,'other_ingre':other_ingre,'food_cat':food_cat,'btn_color':btn_color,'fats':fats,'cal':cal,'protein':protein,'carbs':carbs,'cholestrol':cholestrol,'unit_c':unit_c,'unit_f':unit_f,'unit_p':unit_p,'unit_ch':unit_ch,'unit_ca':unit_ca,'steps':steps}
    except:
        context={'recipe_item':recipe_item,'other_ingre':other_ingre,'food_cat':food_cat,'btn_color':btn_color,'fats':fats,'cal':cal,'protein':protein,'carbs':carbs,'cholestrol':cholestrol,'unit_c':unit_c,'unit_f':unit_f,'unit_p':unit_p,'unit_ch':unit_ch,'unit_ca':unit_ca,'steps':steps}

    return render(request,'recipes/recipe_detail.html',context)




def exp_recipe(request):
    ex_rec = request.POST.get('recpe')
    url = "https://api.spoonacular.com/recipes/complexSearch?query="+str(ex_rec)+"&number=1&apiKey="+key
    res = requests.get(url)
    result = json.loads(res.content.decode('utf-8'))

    a = result['results']
    b = a[0]

    url = "https://api.spoonacular.com/recipes/"+str(b['id'])+"/ingredientWidget?apiKey="+key
    res1 = requests.get(url)
    result1 = json.loads(res.content.decode('utf-8'))

    return render(request,'recipes/explore_recipe.html')

def save_recipe(request):
    if request.method == "POST":
        form = AddRecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            r_form = AddRecipeForm(request.POST)
            if r_form.is_valid():
                add_recipe = r_form.save(commit=True)
                add_recipe.user = request.user
                add_recipe.image = form.cleaned_data.get("image")
                add_recipe.save()
                return render(request,'recipes/recipie_added.html', context={"recipe_items": True})
            else:
                return render(request,'recipes/recipie_added.html', context={"recipe_items": False})

    else:
        return render(request,'recipes/recipie_added.html', context={"recipe_items": False})
