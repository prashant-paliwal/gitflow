from rest_framework import viewsets
from django.contrib.auth.models import User
from authentication.serializers import UserSerializer

from fastapi import FastAPI
app = FastAPI()

# Create your views here.

class Users(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer