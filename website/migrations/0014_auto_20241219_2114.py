# Generated by Django 3.2.19 on 2024-12-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20241219_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonstats',
            name='all_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lessonstats',
            name='month_bonus',
            field=models.IntegerField(default=0),
        ),
    ]