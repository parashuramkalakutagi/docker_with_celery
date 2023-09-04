import datetime

from django.db import models
from datetime import timedelta
from django.utils import timezone
class Story(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(timezone.now() + datetime.timedelta(minutes=5))