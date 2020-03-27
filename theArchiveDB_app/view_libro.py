# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializer import *
from .models import *
from django.shortcuts import get_object_or_404


class BookList(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        book_list = Libro.objects.all()
        book_list_data = BookSerializer(book_list, many=True).data
        return Response(book_list_data)

    def post(self, request):
        b = Libro.objects.get(identifier=request.data.get("identifier"))

        if request.method == "POST":
            libro_obj = Libro(user_id=request.data.get("identifier"))
            libro_obj.save()
        return Response({"status": "success", "response": "Libro Successfully Created"},
                        status=status.HTTP_201_CREATED)


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


class MyBookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self, request):
        return Libro.objects.filter(identifier=self.request.data)
