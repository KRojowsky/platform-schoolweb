# Generated by Django 3.2.19 on 2023-11-08 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0062_post_participants_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='participants_count',
        ),
    ]