# Generated by Django 3.2.19 on 2023-11-08 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0051_auto_20231108_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='participants_count',
            new_name='num_participants',
        ),
    ]
