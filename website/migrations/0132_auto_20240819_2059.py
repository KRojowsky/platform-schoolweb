# Generated by Django 3.2.19 on 2024-08-19 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0131_auto_20240819_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(default='Brak opisu', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
