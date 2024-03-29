# Generated by Django 3.2.19 on 2023-11-12 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0091_auto_20231112_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lessoncorrection',
            options={},
        ),
        migrations.AddField(
            model_name='lessoncorrection',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lessoncorrection',
            name='attended_students',
            field=models.ManyToManyField(blank=True, related_name='attended_students', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lessoncorrection',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.post'),
        ),
    ]
