from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, LoginSerializer
from .models import User

# Create your views here.
class UserCreateView(CreateAPIView):
  serializer_class = UserSerializer
  permission_classes = (AllowAny,)

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    status_code = status.HTTP_201_CREATED
    response = {
      'user': serializer.data,
      'status': status_code,
      'message': 'We did it!'
    }
    
    return Response(response, status_code)

class UserView(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class LoginView(CreateAPIView):
  serializer_class = LoginSerializer
  permission_classes = (AllowAny,)

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    status_code = status.HTTP_200_OK
    response = {
      'email': serializer.data['email'],
      'token': serializer.data['token'],
      'status': status_code,
      'message': 'Logged in!'
    }
    
    return Response(response, status_code)