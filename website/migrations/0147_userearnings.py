# Generated by Django 3.2.19 on 2024-12-08 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0146_delete_teacherearnings'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEarnings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_earnings', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_earnings', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='earnings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Earnings',
                'verbose_name_plural': 'User Earnings',
            },
        ),
    ]
