"""
Views for the recipe APIs.
"""
# Importing the base class ModelViewSet for creating a view that handles CRUD operations on a model.
from rest_framework import (
    viewsets,
    mixins,
)
# Importing token-based authentication for the API.
from rest_framework.authentication import TokenAuthentication
# Importing a permission class to ensure that only authenticated users can access the view.
from rest_framework.permissions import IsAuthenticated
from core.models import (
    Recipe,
    Tag,
)
# Importing serializer class (RecipeSerializer) from the recipe app,
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

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)


class TagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Manage tags in the database."""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-name')
