# Generated by Django 3.2.19 on 2024-02-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0121_user_all_lessons_intermediate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(default='Brak opisu', null=True),
        ),
    ]
