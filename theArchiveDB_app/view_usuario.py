from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializer import *
from .models import *
import datetime
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


class UserList(APIView):
    # permission_classes = (IsAuthenticated,)

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
            user_detail.set_password(str(request.data.get('password')))
            feed_obj = Update(username=username, type=4, date=datetime.date.today())
            user_detail.save()
            feed_obj.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
