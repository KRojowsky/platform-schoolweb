# Generated by Django 3.2.19 on 2023-11-09 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0072_post_room_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='room_members',
        ),
        migrations.AddField(
            model_name='roommember',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.post'),
        ),
    ]