from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class GiftBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftBox
        fields = '__all__'
