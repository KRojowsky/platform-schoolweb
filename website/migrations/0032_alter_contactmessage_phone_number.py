# Generated by Django 3.2.19 on 2023-09-09 17:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_contactmessage_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Numer telefonu musi byc w formacie: '999 999 999'. Maksymalnie 15 cyfr.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]