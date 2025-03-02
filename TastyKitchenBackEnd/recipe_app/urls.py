from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, register_user
from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name="register"),
    path('login/', ObtainAuthToken.as_view(), name="login"),
]
