# Generated by Django 3.2.19 on 2023-11-08 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0050_room_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='is_deleted',
        ),
        migrations.AddField(
            model_name='post',
            name='participants_count',
            field=models.IntegerField(default=0),
        ),
    ]
