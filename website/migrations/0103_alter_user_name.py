# Generated by Django 3.2.19 on 2023-12-01 08:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0102_auto_20231128_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True, validators=[django.core.validators.MaxLengthValidator(limit_value=10)]),
        ),
    ]