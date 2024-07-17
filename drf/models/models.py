from django.db import models

# Create your models here.

class Chef(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    years_of_experience = models.IntegerField()

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    cooking_time = models.DateField()
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    calories_per_100g = models.IntegerField()
    type = models.CharField(max_length=50)
    dishes = models.ManyToManyField(Dish, related_name='ingredients')

    def __str__(self):
        return self.name

