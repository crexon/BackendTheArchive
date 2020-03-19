from rest_framework import serializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'password', 'name', 'surname', 'email')

    def save(self):
        account = Usuario(
            username=self.validated_data['username'],
            password=self.validated_data['password'],
            name=self.validated_data['name'],
            surname=self.validated_data['surname'],
            email=self.validated_data['email'],
        )
        # account.set_password(password)
        account.save()
        return account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'password', 'name', 'surname', 'email')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
