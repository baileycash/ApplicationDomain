from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from .serializer import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = ('TokenAuthentication',)


    # def post(self)





class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# @api_view(['POST'])
# def register_user_view(request):
#     if len(request.data['username']) == 0:
#         return Response({
#             'username' : ['must enter username!']
#         }, status = status.HTTP_400_BAD_REQUEST)
#
#     if len(request.data['password']) == 0:
#         return Response({
#             'password' : ['must enter password!']
#         }, status = status.HTTP_400_BAD_REQUEST)
#
#     if request.data['password'] != request.data['confirm_password']:
#         return Response({
#             'password' : ['passwords must match!']
#         }, status = status.HTTP_400_BAD_REQUEST)
#
#     user = User.objects.create_user(
#         request.data['username'],
#         None,
#         request.data['password'])
#
#     user.is_active = False
#     user.save()
#
#     return Response(UserSerializer(user, context={ 'request' : request }).data)
