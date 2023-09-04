from celery import shared_task
from datetime import timedelta
# from datetime import timezone
from .models import Story
from celery_django import settings
from django.utils import timezone

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "DONE "


@shared_task(bind=True)
def new_func(self):
    for i in range(5,90):
        print(i)
    return "DONE "



@shared_task(bind= True)
def delete_old_story(self):
    stories = Story.objects.all()
    for story in stories:
        if story.expiration_date < timezone.localtime(timezone.now()):
            story.delete()
    return " story deleted"

