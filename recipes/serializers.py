from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id", "name", "time", "description", "ingredients", "parent_id"]
        depth = 3  # TODO
