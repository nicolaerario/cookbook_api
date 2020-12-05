from rest_framework import filters, viewsets

from . import models
from . import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    search_fields = ["ingredients"]
    filter_backends = (filters.SearchFilter,)
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
