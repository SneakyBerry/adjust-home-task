# Generated by Django 4.0.2 on 2022-02-06 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Adjust",
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
                ("date", models.DateField(db_index=True)),
                ("channel", models.TextField(db_index=True)),
                ("country", models.CharField(db_index=True, max_length=2)),
                (
                    "os",
                    models.TextField(
                        choices=[("ios", "Apple iOS"), ("android", "Android OS")],
                        db_index=True,
                    ),
                ),
                ("impressions", models.PositiveIntegerField(db_index=True)),
                ("clicks", models.PositiveIntegerField(db_index=True)),
                ("installs", models.PositiveIntegerField(db_index=True)),
                ("spend", models.FloatField(db_index=True)),
                ("revenue", models.FloatField(db_index=True)),
            ],
        ),
    ]
