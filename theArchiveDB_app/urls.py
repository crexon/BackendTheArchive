from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from theArchiveDB_app.view_usuario import (Register, UserDetail, UserList)
from theArchiveDB_app.view_libro import (BookList, BookDetail)
from theArchiveDB_app.view_feed import (FeedList)
from theArchiveDB_app.view_estanteria import (EstanteriaDetail, EstanteriaList, EstanteriaByType, DeleteEstanteria)

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

    #ESTANTERIA
    path('estanteria/', EstanteriaList.as_view(), name="Listado de estaneria"),
    path('estanteria/<slug:username>', EstanteriaDetail.as_view(), name="Listado de estaneria por usuario"),
    path('estanteria/<int:state>/<slug:username>', EstanteriaByType.as_view(), name="Listado libros"),
    path('estanteria/<slug:username>/<slug:idbook>', DeleteEstanteria.as_view(), name="Eliminar libros"),

    #FEED
    path('feed/', FeedList.as_view(), name="Historial de acciones")
]