from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from .serializer import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = ('TokenAuthentication',)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
