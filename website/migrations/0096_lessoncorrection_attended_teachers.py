# Generated by Django 3.2.19 on 2023-11-12 18:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0095_auto_20231112_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessoncorrection',
            name='attended_teachers',
            field=models.ManyToManyField(blank=True, related_name='attended_teachers', to=settings.AUTH_USER_MODEL),
        ),
    ]