# Generated by Django 3.2.19 on 2023-11-12 14:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0088_auto_20231112_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='attended_students',
            field=models.ManyToManyField(blank=True, related_name='attended_lessons', to=settings.AUTH_USER_MODEL),
        ),
    ]
