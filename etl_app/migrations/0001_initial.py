# Generated by Django 4.1.2 on 2023-06-05 03:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Compound",
            fields=[
                ("compound_id", models.IntegerField(primary_key=True, serialize=False)),
                ("compound_name", models.CharField(max_length=255)),
                ("compound_structure", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Experiment",
            fields=[
                (
                    "experiment_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("user_id", models.IntegerField()),
                ("experiment_compound_ids", models.CharField(max_length=255)),
                ("experiment_run_time", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("signup_date", models.DateField()),
            ],
        ),
    ]
