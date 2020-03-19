from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from theArchiveDB_app.views import (registration_view, UserDetail, UserList, BookList, BookDetail)

app_name = "Archive"

urlpatterns = [
    #USUARIOS
    path('signup/', registration_view, name="Registrarse"),
    path('user/', UserList.as_view(), name="Listado de usuarios"),
    path('user/<slug:username>', UserDetail.as_view(), name="Usuario"),

    #LIBROS
    path('book/', BookList.as_view(), name="Listado de libros"),
    path('book/<int:pk>', BookDetail.as_view(), name="Libro"),
]