# Generated by Django 3.2.19 on 2023-11-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0082_user_break_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='all_break_lessons',
            field=models.IntegerField(default=0),
        ),
    ]