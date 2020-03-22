from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from theArchiveDB_app.views import (Register, UserDetail, UserList, BookList, BookDetail)

app_name = "Archive"

urlpatterns = [
    #USUARIOS
    path('signup/', Register.as_view(), name="Registrarse"),
    path('login/', obtain_auth_token, name="Login"),

    path('user/', UserList.as_view(), name="Listado de usuarios"),
    path('user/<slug:username>', UserDetail.as_view(), name="Usuario"),

    #LIBROS
    path('book/', BookList.as_view(), name="Listado de libros"),
    path('book/<int:pk>', BookDetail.as_view(), name="Libro"),
]