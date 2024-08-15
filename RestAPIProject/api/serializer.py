#serializer.py tells python how to transform our model to JSON Data that we can access in our API
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'