from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .tasks import send_mail_func

class send_mail_to_all(viewsets.ViewSet):
    def list(self,request):
        send_mail_func.delay()
        return Response({'msg':'mail has been sent to all users...'})