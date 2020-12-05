from django.db import router
from .views import RecipeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", RecipeViewSet, basename="recipes")
urlpatterns = router.urls
