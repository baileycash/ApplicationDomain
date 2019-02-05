from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializer import UserSerializer
# from .models import Movie


# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
