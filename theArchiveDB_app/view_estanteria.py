from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *
import datetime
from .models import *


class EstanteriaList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        estanteria_list = Estanteria.objects.all()
        estanteria_list_data = EstanteriaSerializer(estanteria_list, many=True).data
        return Response(estanteria_list_data)

    def post(self, request):
        u = User.objects.get(username=request.data.get("username"))

        if request.method == "POST":

            if Libro.objects.filter(identifier=request.data.get("identifier")).exists():
                b = Libro.objects.get(identifier=request.data.get("identifier"), title=request.data.get("title"),
                                      authors=request.data.get("authors"), publisher=request.data.get("publisher"),
                                      description=request.data.get("description"),
                                      publishedDate=request.data.get("publishedDate"),
                                      pageCount=request.data.get("pageCount"),
                                      categories=request.data.get("categories"),
                                      thumbnail=request.data.get("thumbnail"))
                if Estanteria.objects.filter(user_id=u,
                                             book_id=b).exists():
                    return Response(status=status.HTTP_306_RESERVED)

                else:
                    estanteria_obj = Estanteria(user_id=u, book_id=b, state=request.data.get("state"),
                                                progress=request.data.get("progress"),
                                                recommendation=request.data.get("recommendation"))

                    feed_obj = Update(username=u.username, type=request.data.get("state"), date=datetime.date.today())

                    estanteria_obj.save()
                    feed_obj.save()

            else:
                b = Libro(identifier=request.data.get("identifier"), title=request.data.get("title"),
                          authors=request.data.get("authors"), publisher=request.data.get("publisher"),
                          description=request.data.get("description"),
                          publishedDate=request.data.get("publishedDate"),
                          pageCount=request.data.get("pageCount"), categories=request.data.get("categories"),
                          thumbnail=request.data.get("thumbnail"))
                b.save()
                estanteria_obj = Estanteria(user_id=u, book_id=b, state=request.data.get("state"),
                                            progress=request.data.get("progress"),
                                            recommendation=request.data.get("recommendation"))
                estanteria_obj.save()

                feed_obj = Update(username=u.username, type=request.data.get("state"), date=datetime.date.today())
                feed_obj.save()

        return Response({"status": "success", "response": "Estanteria Successfully Created"},
                        status=status.HTTP_201_CREATED)


class EstanteriaDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username):
        u = User.objects.get(username=username)
        estanteria_list = Estanteria.objects.filter(user_id=u)
        estanteria_list_data = EstanteriaSerializer(estanteria_list, many=True).data
        return Response(estanteria_list_data)


class EstanteriaByType(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, state, username):
        u = User.objects.get(username=username)
        estanteria = Estanteria.objects.filter(user_id=u, state=state)
        book_list = Libro.objects.filter(identifier__in=estanteria.values_list('book_id__identifier'))
        book_list_data = BookSerializer(book_list, many=True).data
        return Response(book_list_data)


class DeleteEstanteria(APIView):

    def delete(self, request, username, idbook):
        u = User.objects.get(username=username)
        book_detail = get_object_or_404(Libro, identifier=idbook)
        estantera_detail = get_object_or_404(Estanteria, user_id=u, book_id=book_detail)
        estantera_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
