# Generated by Django 3.2.19 on 2024-11-19 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0142_user_interests'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Lesson',
        ),
    ]