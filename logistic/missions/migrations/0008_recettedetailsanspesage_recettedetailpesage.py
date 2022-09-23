# Generated by Django 4.0.6 on 2022-08-29 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0007_remove_recettedetailpesage_recettes_ptr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecetteDetailSansPesage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_recette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infos_snsPesee', to='missions.recettes')),
            ],
            options={
                'ordering': ['-id_recette'],
            },
        ),
        migrations.CreateModel(
            name='RecetteDetailPesage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premier_pese', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('deuxieme_pese', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('id_recette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infos_pesee', to='missions.recettes')),
            ],
        ),
    ]
