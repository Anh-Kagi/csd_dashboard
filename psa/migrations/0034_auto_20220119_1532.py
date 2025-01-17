# Generated by Django 3.2.11 on 2022-01-19 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psa', '0033_auto_20211222_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='corvetproduct',
            name='cvm2',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'CVM2'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corvet_cvm2', to='psa.ecu'),
        ),
        migrations.AlterField(
            model_name='ecu',
            name='type',
            field=models.CharField(choices=[('BSI', 'Boitier Servitude Intelligent'), ('BSM', 'Boitier Servitude Moteur'), ('CMB', 'Combine Planche de Bord'), ('CMM', 'Calculateur Moteur Multifonction'), ('EMF', 'Ecran Multifonctions'), ('FMUX', 'Façade Multiplexée'), ('HDC', 'Haut de Colonne de Direction (COM200x)'), ('MDS', 'Module de service telematique'), ('CVM2', 'Camera Video Multifonction V2')], max_length=7, verbose_name='type'),
        ),
    ]
