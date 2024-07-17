from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Chef, Dish, Ingredient
from .serializers import ChefSerializer, DishSerializer, IngredientSerializer

# Create your views here.
class ChefAPIView(APIView):
    def get(self, request):
        w = Chef.objects.all()
        return Response({'posts': ChefSerializer(w, many=True).data})

    def post(self, request):
        serializer = ChefSerializer(data=request.cooking_time)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            isinstance = Chef.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ChefSerializer(data=request.cooking_time, instance=isinstance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = Chef.objects.get(pk=pk)
        except Chef.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DishGenericsView(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishGenericsUpdate(generics.UpdateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsAuthenticated, )

class DishGenericsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer