# Generated by Django 3.2.19 on 2024-12-28 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_newstudents_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newstudents',
            name='courses',
        ),
    ]