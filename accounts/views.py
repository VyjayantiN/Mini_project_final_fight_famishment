from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import QueryDict
import json
from urllib.parse import unquote
import urllib
from .models import recipe,gen_ins,FoodItem
import pandas as pd
import joblib
from .ml_models import train_model
from sklearn.model_selection import train_test_split
# Create your views here.
def home(request):
    return render(request,'accounts/index.html')
def about(request):
    return render(request,'accounts/about2.html')
def features(request):
    return render(request,'accounts/features.html')
def child_bmi(request):
    return render(request,'accounts/child_bmi.html')
def blog(request):
    return render(request,'accounts/blog.html')
def usermain(request):
    if request.method=='POST':
        height=request.POST['height']
        weight=request.POST['weight']
        age=request.POST['age']
        district=request.POST['district']
        gender=request.POST['gender']
        category=""
        print(request.POST)
        bmi = int(weight) / ((int(height)/100) ** 2)
        print(bmi)
        if gender.lower() == "male":
            if gender.lower() == "male":
                if bmi < 18.5:
                    category = "Underweight"
                elif bmi > 25.5:
                    category = "Overweight"
                else:
                    category = "Healthy"
        elif gender.lower() == "female":
                if bmi < 18.5:
                    category = "Underweight"
                elif bmi > 25.5:
                    category = "Overweight"
                else:
                    category = "Healthy"

        else:
            category = "Unknown gender"
        object_1=recipe.objects.filter(district=district,age=age)
        object_2=gen_ins.objects.filter(age=age)
        for obj in object_2:
            return render(request,'accounts/usermain.html',{'obj1':object_1,'instructions':obj.instructions,'food_items':obj.food_items,'mal_instructions':obj.mal_ins,'category':category})

def items_home(request):
    my_data = request.GET.get('data', '')
    object_1=recipe.objects.filter(recipe_name=my_data)
    for obj in object_1:
        return render(request,'accounts/item2.html',{'recipe_name':my_data,'ins':obj.ins,'calories':obj.calories,'people_served':obj.people_served,'difficulty':obj.difficulty, 'ing':obj.ing})

def post1(request):
    return render(request,'accounts/post1.html')
def post2(request):
    return render(request,'accounts/post2.html')
def post3(request):
    return render(request,'accounts/post3.html')
def post4(request):
    return render(request,'accounts/post4.html')
def post5(request):
    return render(request,'accounts/post5.html')
def post6(request):
    return render(request,'accounts/post6.html')

def yoga1(request):
    return render(request,'accounts/yoga1.html')
def yoga2(request):
    return render(request,'accounts/yoga2.html')
def yoga3(request):
    return render(request,'accounts/yoga3.html')
def yoga4(request):
    return render(request,'accounts/yoga4.html')
def bmi(request):
    return render(request,'accounts/bmi.html')
def bmi_predicted(request):
    if request.method == 'POST':
        # Retrieve form data
        model = joblib.load('accounts/linear_regression_model.pkl')
        height = int(request.POST['height'])
        weight = int(request.POST['weight'])
        rice_quantity = int(request.POST['rice'])
        roti_quantity = int(request.POST['roti'])
        dal_quantity = int(request.POST['dal'])
        eggs_quantity = int(request.POST['eggs'])
        sabzi_quantity = int(request.POST['sabzi'])
        fruits_quantity = int(request.POST['fruits'])
        buttermilk_quantity = int(request.POST['buttermilk'])
        juice_quantity = int(request.POST['juice'])
        workout=int(request.POST['workout'])
        # Calculate total nutrients and calories
        total_proteins = rice_quantity * 2.6 + roti_quantity * 3 + dal_quantity * 8.9 + eggs_quantity * 6 + sabzi_quantity * 2 + fruits_quantity * 0.6 + buttermilk_quantity * 2 + juice_quantity * 0.5
        total_fats = rice_quantity * 0.3 + roti_quantity * 1 + dal_quantity * 0.4 + eggs_quantity * 5.3 + sabzi_quantity * 4 + fruits_quantity * 0.5 + buttermilk_quantity * 1.5 + juice_quantity * 0.2
        total_carbohydrates = rice_quantity * 28 + roti_quantity * 15 + dal_quantity * 20 + eggs_quantity * 1.1 + sabzi_quantity * 8 + fruits_quantity * 15 + buttermilk_quantity * 10 + juice_quantity * 25
        total_vitamins = rice_quantity * 0.1 + roti_quantity * 0.2 + dal_quantity * 0.4 + eggs_quantity * 0.1 + sabzi_quantity * 0.2 + fruits_quantity * 0.1 + buttermilk_quantity * 0.3 + juice_quantity * 0.2
        total_minerals = rice_quantity * 0.5 + roti_quantity * 0.3 + dal_quantity * 0.2 + eggs_quantity * 0.1 + sabzi_quantity * 1 + fruits_quantity * 0.3 + buttermilk_quantity * 0.7 + juice_quantity * 0.5
        total_calories = rice_quantity * 130 + roti_quantity * 80 + dal_quantity * 104 + eggs_quantity * 78 + sabzi_quantity * 120 + fruits_quantity * 60 + buttermilk_quantity * 42 + juice_quantity * 100

        # Calculate BMI
        bmi = int(weight / ((height / 100) ** 2))
        protein_percentage = (total_proteins / 1000) * 100
        carbohydrate_percentage = (total_carbohydrates / 5000) * 100
        fat_percentage = (total_fats / 2000) * 100 

        total_nutrients = total_proteins + total_fats + total_carbohydrates + total_vitamins + total_minerals
        protein_percentage2 = (total_proteins / total_nutrients) * 100
        carbohydrate_percentage2 = (total_carbohydrates / total_nutrients) * 100
        fat_percentage2 = (total_fats / total_nutrients) * 100
        vitamin_percentage2 = (total_vitamins / total_nutrients) * 100
        mineral_percentage2 = (total_minerals / total_nutrients) * 100
        # Render results in a new HTML page


        

        # Load your dataset containing BMI values
        # For example, if you have a CSV file with BMI values, you can load it using pandas
        dataset = pd.read_csv('accounts/dataset_2nd_april.csv')

        # Extract the corresponding BMI values from the dataset
        X = dataset.drop('BMI After 30 Days' , axis=1)
        y = dataset['BMI After 30 Days']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # Train the model
        model = train_model(X_train, y_train)

        # Save the trained model
        joblib.dump(model, 'accounts/linear_regression_model.pkl')

        # Make predictions
        predicted_bmi = model.predict([[bmi,total_calories,workout]])
        return render(request, 'accounts/bmi_predicted.html', {
            'bmi': bmi,
            'total_proteins': total_proteins,
            'total_fats': total_fats,
            'total_carbohydrates': total_carbohydrates,
            'total_vitamins': total_vitamins,
            'total_minerals': total_minerals,
            'total_calories': total_calories,
            'protein_percentage': protein_percentage,
            'carbohydrate_percentage': carbohydrate_percentage,
            'fat_percentage': fat_percentage,
            'protein_percentage2': protein_percentage2,
            'carbohydrate_percentage2': carbohydrate_percentage2,
            'fat_percentage2': fat_percentage2,
            'vitamin_percentage2': vitamin_percentage2,
            'mineral_percentage2': mineral_percentage2,
            'workout':workout,
            'predicted_bmi': predicted_bmi[0],
        })
