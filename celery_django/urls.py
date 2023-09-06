
from django.contrib import admin
from home.views import *
import send_mail.urls
from rest_framework.routers import DefaultRouter
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static

router  = DefaultRouter()

router.register('Celery_testing',Celery_testing,basename='Celery_testing')
router.register('StoryViewset',StoryViewset,basename='StoryViewset')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('mail/',include(send_mail.urls)),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
