# Generated by Django 3.2.19 on 2023-10-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0042_post_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='schoolweb_rating',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True),
        ),
    ]