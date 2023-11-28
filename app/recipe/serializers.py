"""
Serializers for recipe APIs.
"""

from rest_framework import serializers
from core.models import Recipe

# This serializer will be used to convert Recipe model instances to JSON and vice versa.
class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        # The fields attribute is a list of fields from the Recipe model that
        # should be included in the serialized output.
        fields = ['id', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']

class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']