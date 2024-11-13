from django.db import models

class recipe(models.Model):
    recipe_name=models.CharField(max_length=100,null=True)
    people_served=models.TextField(null=True)
    calories= models.TextField(null=True)
    difficulty = models.TextField(null=True)
    ing=models.TextField(null=True)
    ins=models.TextField(null=True)
    age=models.CharField(max_length=20,null=True)
    category=models.CharField(max_length=50,null=True)
    district=models.CharField(max_length=50,null=True)
class gen_ins(models.Model):
    instructions=models.TextField()
    food_items=models.TextField()
    mal_ins=models.TextField()
    age=models.CharField(max_length=20,null=True)

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    proteins = models.FloatField()
    vitamins = models.FloatField()
    minerals = models.FloatField()
    carbohydrates = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()