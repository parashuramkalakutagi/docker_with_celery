#!/bin/sh

python manage.py makemigrations
python manage.py migrate



gunicorn -b 0.0.0.0 -p 8000 celery_django.wsgi:application
celery -A celery_django.celery worker --pool=solo -l info
celery -A DjangoLib beat -l info