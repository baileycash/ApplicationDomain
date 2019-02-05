from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from .models import Movie

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only': True, 'required': True }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# class MovieSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('id', 'title', 'description', 'year')
