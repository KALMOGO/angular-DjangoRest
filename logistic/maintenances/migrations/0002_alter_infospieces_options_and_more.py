# Generated by Django 4.1 on 2022-08-31 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maintenances", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="infospieces",
            options={"ordering": ["maintenanceConcernee", "-date_creation"]},
        ),
        migrations.AlterModelOptions(
            name="piecesechanges", options={"ordering": ["nom", "-date_creation"]},
        ),
        migrations.AlterField(
            model_name="piecesechanges",
            name="nom",
            field=models.CharField(max_length=250, unique=True),
        ),
    ]