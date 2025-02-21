"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from models.views import ChefAPIView, DishGenericsView, DishGenericsDetail, DishGenericsUpdate, IngredientViewSet

router = routers.SimpleRouter()
router.register(r'ingredient', IngredientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cheflist/', ChefAPIView.as_view()),
    path('api/v1/cheflist/<int:pk>/', ChefAPIView.as_view()),
    path('api/v1/dishlist/', DishGenericsView.as_view()),
    path('api/v1/dishlist/<int:pk>', DishGenericsUpdate.as_view()),
    path('api/v1/dishdetail/<int:pk>', DishGenericsDetail.as_view()),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
