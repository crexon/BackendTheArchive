# Create your views here.
from django.db.models.functions import Trunc
from rest_framework.fields import DateField
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from .models import *


class FeedList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        feed_list = Update.objects.all().order_by('-date')
        feed_list_data = FeedSerializer(feed_list, many=True).data
        return Response(feed_list_data)
