# Generated by Django 3.2.19 on 2023-11-10 08:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0076_remove_post_participants_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='count_members',
            field=models.ManyToManyField(blank=True, related_name='LessonMembers', to=settings.AUTH_USER_MODEL),
        ),
    ]
