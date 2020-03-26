from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializer import *
from .models import *


class EstanteriaList(APIView):

    def get(self, request):
        estanteria_list = Estanteria.objects.all()
        estanteria_list_data = EstanteriaSerializer(estanteria_list, many=True).data
        return Response(estanteria_list_data)

    def post(self, request):
        u = User.objects.get(username=request.data.get("username"))
        b = Libro.objects.get(identifier=request.data.get("identifier"))

        if request.method == "POST":
            estanteria_obj = Estanteria(user_id=u, book_id=b, state=request.data.get("state"),
                                        recommendation=request.data.get("recommendation"))
            estanteria_obj.save()
        return Response({"status": "success", "response": "Estanteria Successfully Created"},
                        status=status.HTTP_201_CREATED)


class EstanteriaDetail(APIView):
    def get(self, request, username):
        u = User.objects.get(username=username)
        estanteria_list = Estanteria.objects.filter(user_id=u)
        estanteria_list_data = EstanteriaSerializer(estanteria_list, many=True).data
        return Response(estanteria_list_data)
