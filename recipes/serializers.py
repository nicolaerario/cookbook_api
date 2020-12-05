from rest_framework import serializers
from .models import Recipe


class RecipeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id", "name", "time", "description", "ingredients", "parent_id"]
        depth = 9


class RecipeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id", "name", "time", "description", "ingredients", "parent_id"]
