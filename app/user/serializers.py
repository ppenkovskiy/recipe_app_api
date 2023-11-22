"""
Serializers for the user API view.
"""
from django.contrib.auth import get_user_model
# import serialize module from rest framework
from rest_framework import serializers

# serealize is simply just a way to convert objects to and from python objects
class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        # Specify the fields that we want to enable for the serializer
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
