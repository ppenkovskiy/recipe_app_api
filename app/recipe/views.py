"""
Views for the recipe APIs.
"""
# Importing the base class ModelViewSet for creating a view that handles CRUD operations on a model.
from rest_framework import viewsets
# Importing token-based authentication for the API.
from rest_framework.authentication import TokenAuthentication
# Importing a permission class to ensure that only authenticated users can access the view.
from rest_framework.permissions import IsAuthenticated
# Importing the Recipe model from the core app. This assumes that there's a
# model named Recipe in the core app, and this view is designed to work with it.
from core.models import Recipe
# Importing the serializer class (RecipeSerializer) from the recipe app,
# which is used to serialize/deserialize Recipe objects.
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""

    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            # Return a reference to the class
            return serializers.RecipeSerializer
        return self.serializer_class
