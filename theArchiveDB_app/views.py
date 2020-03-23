# Create your views here.
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializer import *
from .models import *
from django.shortcuts import get_object_or_404


class Register(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        user = User.objects.create(
            username=request.data.get('username'),
            first_name=request.data.get('name'),
            last_name=request.data.get('surname'),
        )
        user.set_password(str(request.data.get('password')))
        user.save()
        return Response({"status": "success", "response": "User Successfully Created"}, status=status.HTTP_201_CREATED)


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
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_list = User.objects.all()
        user_list_data = UserSerializer(user_list, many=True).data
        return Response(user_list_data)


class UserDetail(APIView):
    def get(self, request, username):
        user_detail = get_object_or_404(User, username=username)
        user_detail_data = UserSerializer(user_detail).data
        return Response(user_detail_data)

    def delete(self, request, username):
        user_detail = get_object_or_404(User, username=username)
        user_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, username):
        user_detail = get_object_or_404(User, username=username)
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
