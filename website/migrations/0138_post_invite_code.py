# Generated by Django 5.1 on 2024-10-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0137_alter_blogcategory_image_alter_blogpost_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='invite_code',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
