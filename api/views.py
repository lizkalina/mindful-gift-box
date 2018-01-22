from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class GiftBoxViewSet(viewsets.ModelViewSet):
    queryset = GiftBox.objects.all()
    serializer_class = GiftBoxSerializer
