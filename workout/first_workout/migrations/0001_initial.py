# Generated by Django 4.1.2 on 2022-10-19 10:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Workouts",
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
                ("title", models.CharField(max_length=50)),
                (
                    "workout_time",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(
                                3600, "Значение не должно превышать 3600 секунд."
                            )
                        ]
                    ),
                ),
                ("short_info", models.TextField(max_length=400)),
                ("full_info", models.TextField(max_length=1000)),
                ("img", models.ImageField(upload_to="")),
            ],
        ),
    ]
