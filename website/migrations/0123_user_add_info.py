# Generated by Django 3.2.19 on 2024-02-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0122_alter_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='add_info',
            field=models.TextField(default='Dodaj opis...', null=True),
        ),
    ]