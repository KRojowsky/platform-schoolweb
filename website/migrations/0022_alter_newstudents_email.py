# Generated by Django 3.2.19 on 2024-12-29 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_newstudents_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newstudents',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
