# Generated by Django 3.2.19 on 2023-11-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0083_user_all_break_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='all_missed_lessons',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='missed_lessons',
            field=models.IntegerField(default=0),
        ),
    ]
