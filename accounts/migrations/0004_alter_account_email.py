# Generated by Django 4.1.4 on 2022-12-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_account_shift"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="email",
            field=models.EmailField(max_length=127, unique=True),
        ),
    ]
