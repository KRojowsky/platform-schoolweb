# Generated by Django 3.2.19 on 2024-12-08 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0151_auto_20241208_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersearning',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='earnings', to=settings.AUTH_USER_MODEL),
        ),
    ]
