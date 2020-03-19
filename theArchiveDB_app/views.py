# Create your views here.
from rest_framework import status, viewsets
from theArchiveDB_app.serializer import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .serializer import *
from .models import *
from django.shortcuts import get_object_or_404


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Nuevo usuario registrado correctamente'
            data['username'] = account.username
            data['email'] = account.email
        else:
            data = serializer.errors
        return Response(data)


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    data = {}
    if user is not None:
        login(request, user)
        data['response'] = 'Login correcto'
    else:
        data['response'] = 'Login incorrecto'
    return Response(data)


class UserList(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_list = Usuario.objects.all()
        user_list_data = UserSerializer(user_list, many=True).data
        return Response(user_list_data)


class UserDetail(APIView):
    def get(self, request, username):
        user_detail = get_object_or_404(Usuario, username=username)
        user_detail_data = UserSerializer(user_detail).data
        return Response(user_detail_data)

    def delete(self, request, username):
        user_detail = get_object_or_404(Usuario, username=username)
        user_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, username):
        user_detail = get_object_or_404(Usuario, username=username)
        serializer = UserSerializer(user_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookList(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        book_list = Libro.objects.all()
        book_list_data = BookSerializer(book_list, many=True).data
        return Response(book_list_data)


class BookDetail(APIView):
    def get(self, request, pk):
        book_detail = get_object_or_404(Libro, pk=pk)
        book_detail_data = BookSerializer(book_detail).data
        return Response(book_detail_data)

    def delete(self, request, pk):
        book_detail = get_object_or_404(Libro, pk=pk)
        book_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        book_detail = get_object_or_404(Libro, pk=pk)
        serializer = BookSerializer(book_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


