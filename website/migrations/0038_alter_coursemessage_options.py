# Generated by Django 3.2.19 on 2023-10-04 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0037_alter_user_all_lessons'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursemessage',
            options={'ordering': ['messageUpdated', 'messageCreated']},
        ),
    ]
