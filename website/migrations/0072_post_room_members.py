# Generated by Django 3.2.19 on 2023-11-09 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0071_remove_post_participants_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='room_members',
            field=models.ManyToManyField(blank=True, related_name='post_room_members', to='website.RoomMember'),
        ),
    ]
