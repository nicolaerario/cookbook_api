from rest_framework import filters, viewsets

from . import models
from . import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    search_fields = ["ingredients"]
    filter_backends = (filters.SearchFilter,)
    queryset = models.Recipe.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "PUT" or method == "POST":
            return serializers.RecipeWriteSerializer
        else:
            return serializers.RecipeReadSerializer
