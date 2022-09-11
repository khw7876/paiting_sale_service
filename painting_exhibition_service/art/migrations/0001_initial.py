# Generated by Django 4.1.1 on 2022-09-11 18:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("applicant", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArtModel",
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
                ("name", models.CharField(max_length=64, verbose_name="작품명")),
                (
                    "number",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(500),
                        ],
                        verbose_name="호수",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="가격",
                    ),
                ),
                ("create_date", models.DateTimeField(auto_now_add=True)),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="applicant.artist",
                    ),
                ),
            ],
            options={"db_table": "art",},
        ),
    ]
