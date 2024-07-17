from rest_framework import serializers
from .models import Chef, Dish, Ingredient

class ChefSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    years_of_experience = serializers.IntegerField()

    def create(self, validated_data):
        return Chef.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.years_of_experience = validated_data.get("work_expierence", instance.years_of_experience)
        instance.save()
        return instance

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
        depth = 1

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'









