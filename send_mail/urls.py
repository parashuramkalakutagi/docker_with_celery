
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router  = DefaultRouter()

router.register('send_mail_to_all',send_mail_to_all,basename='send_mail_to_all')

urlpatterns = [

    path('',include(router.urls)),
]