# Generated by Django 4.1.7 on 2023-03-03 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Complaint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "appointment_type",
                    models.CharField(
                        choices=[
                            ("passport", "Passport"),
                            ("id", "ID"),
                            ("driverslicence", "Driver's Licence"),
                            ("utilitybill", "Utility Bill"),
                        ],
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
