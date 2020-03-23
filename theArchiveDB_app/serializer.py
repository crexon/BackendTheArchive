from rest_framework import serializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        # fields = ('username', 'password', 'name', 'surname', 'email')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
