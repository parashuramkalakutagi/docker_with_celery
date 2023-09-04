import datetime

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .tasks import test_func , new_func
from datetime import timedelta
from django.utils import timezone
from .models import *
from .serializer import *
from rest_framework.status import *

class Celery_testing(viewsets.ViewSet):
    def list(self,request):
        test_func.delay()
        new_func.delay()
        return Response({'msg':'DONE'})


class StoryViewset(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

