# Generated by Django 4.1.1 on 2022-09-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("missions", "0006_alter_missions_motif"),
    ]

    operations = [
        migrations.RemoveField(model_name="recettedetailpesage", name="recettes_ptr",),
        migrations.RemoveField(
            model_name="recettedetailsanspesage", name="recettes_ptr",
        ),
        migrations.AlterField(
            model_name="missions",
            name="liste_produits",
            field=models.ManyToManyField(
                related_name="liste_produits",
                through="missions.Recettes",
                to="missions.produits",
            ),
        ),
        migrations.AddConstraint(
            model_name="recettes",
            constraint=models.UniqueConstraint(
                fields=("produit", "mission", "client_concerne"),
                name="unique_recette_key",
            ),
        ),
        migrations.DeleteModel(name="RecetteDetailPesage",),
        migrations.DeleteModel(name="RecetteDetailSansPesage",),
    ]
