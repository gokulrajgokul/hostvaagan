# Generated by Django 5.1.7 on 2025-04-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agrivehicles', '0007_rename_owner_location_vehicle_owner_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
