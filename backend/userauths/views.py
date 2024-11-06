from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics,permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from userauths.models import User,Profile
from userauths.serializer import CustomTokenObtainPairSerializer,RegisterSerilizer

# Create your views here.
class CustomTokenObtailPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class=RegisterSerilizer