# Generated by Django 3.2.19 on 2024-02-02 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0116_auto_20240202_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('hour_6_7', models.BooleanField(default=False)),
                ('hour_7_8', models.BooleanField(default=False)),
                ('hour_8_9', models.BooleanField(default=False)),
                ('hour_9_10', models.BooleanField(default=False)),
                ('hour_10_11', models.BooleanField(default=False)),
                ('hour_11_12', models.BooleanField(default=False)),
                ('hour_12_13', models.BooleanField(default=False)),
                ('hour_13_14', models.BooleanField(default=False)),
                ('hour_14_15', models.BooleanField(default=False)),
                ('hour_15_16', models.BooleanField(default=False)),
                ('hour_16_17', models.BooleanField(default=False)),
                ('hour_17_18', models.BooleanField(default=False)),
                ('hour_18_19', models.BooleanField(default=False)),
                ('hour_19_20', models.BooleanField(default=False)),
                ('hour_20_21', models.BooleanField(default=False)),
                ('hour_21_22', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='tutoravailability',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='tutoravailability',
            name='tutor',
        ),
        migrations.DeleteModel(
            name='TimeSlot',
        ),
        migrations.DeleteModel(
            name='TutorAvailability',
        ),
    ]