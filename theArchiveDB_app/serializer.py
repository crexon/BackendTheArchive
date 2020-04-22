from rest_framework import serializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'


class EstanteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estanteria
        fields = '__all__'
