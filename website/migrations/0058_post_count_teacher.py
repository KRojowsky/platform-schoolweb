# Generated by Django 3.2.19 on 2023-11-08 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0057_auto_20231108_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='count_teacher',
            field=models.IntegerField(default=0),
        ),
    ]
