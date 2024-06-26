# Generated by Django 4.1.2 on 2023-03-31 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calculator", "0002_rename_person_personlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Calculation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("expression", models.CharField(max_length=200)),
                ("result", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Memory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.FloatField()),
            ],
        ),
    ]
