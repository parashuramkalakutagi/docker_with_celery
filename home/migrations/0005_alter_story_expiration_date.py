# Generated by Django 4.1.7 on 2023-09-06 04:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_story_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='expiration_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 9, 6, 5, 2, 0, 458896, tzinfo=datetime.timezone.utc)),
        ),
    ]