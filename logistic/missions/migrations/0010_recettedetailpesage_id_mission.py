# Generated by Django 4.0.6 on 2022-09-27 12:45

from django.db import migrations, models
import django.db.models.deletion

# nouveau
class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0009_remove_recettedetailpesage_id_recette_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recettedetailpesage',
            name='id_mission',
            field=models.ForeignKey(default=24, on_delete=django.db.models.deletion.CASCADE, related_name='infos_pesee', to='missions.missions'),
            preserve_default=False,
        ),
    ]