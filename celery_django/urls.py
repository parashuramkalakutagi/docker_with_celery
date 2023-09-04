
from django.contrib import admin
from django.urls import path,include
from home.views import *
import send_mail.urls
from rest_framework.routers import DefaultRouter

router  = DefaultRouter()

router.register('Celery_testing',Celery_testing,basename='Celery_testing')
router.register('StoryViewset',StoryViewset,basename='StoryViewset')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('mail/',include(send_mail.urls)),
]
