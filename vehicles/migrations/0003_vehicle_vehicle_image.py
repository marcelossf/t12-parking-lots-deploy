# Generated by Django 4.1.4 on 2022-12-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicles", "0002_alter_vehicle_spot"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicle",
            name="vehicle_image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
