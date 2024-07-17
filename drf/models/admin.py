from django.contrib import admin

from .models import Chef, Dish, Ingredient

# Register your models here.
admin.site.register(Chef)
admin.site.register(Dish)
admin.site.register(Ingredient)