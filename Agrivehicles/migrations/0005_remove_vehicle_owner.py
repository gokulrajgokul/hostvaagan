# Generated by Django 5.1.7 on 2025-04-09 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agrivehicles', '0004_vehicle_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='owner',
        ),
    ]
