from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from .models import Movie

# class UserCreateSerializer()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'groups', 'last_login', 'is_active')
        extra_kwargs = {'password' : {'write_only': True, 'required': True }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name',)
