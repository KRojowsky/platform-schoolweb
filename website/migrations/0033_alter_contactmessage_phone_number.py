# Generated by Django 3.2.19 on 2023-09-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0032_alter_contactmessage_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
