# Generated by Django 3.2.4 on 2021-06-24 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psa', '0022_auto_20210608_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corvetchoices',
            name='column',
            field=models.CharField(choices=[('DON_LIN_PROD', 'donnee_ligne_de_produit'), ('DON_MAR_COMM', 'donnee_marque_commerciale'), ('DON_SIL', 'donnee_silhouette'), ('DON_GEN_PROD', 'donnee_genre_de_produit'), ('DON_MOT', 'MOTEUR'), ('DON_TRA', 'TRANSMISSION'), ('ATT_DAO', 'SURVEILLANCE VOIE LATERALE'), ('ATT_DGM', 'COMBINE (CARACTERISTIQUES)'), ('ATT_DHB', 'HAUT PARLEUR'), ('ATT_DHG', 'COMMANDE AUTO-RADIO'), ('ATT_DJY', 'SYSTEME NAVIGATION'), ('ATT_DLX', 'AFFICHEUR AV'), ('ATT_DUN', 'AMPLI EQUALISEUR'), ('ATT_DYM', 'PRISE AUXILIAIRE PACK AUDIO'), ('ATT_DYR', 'BOITIER TELEMATIQUE'), ('ATT_DAT', 'ANTENNE'), ('ATT_DCD', 'CARBURANT (RON MINI MOTEUR)'), ('ATT_DCX', 'COTE CONDUITE/POSTE CONDUITE'), ('ATT_DE2', 'MIRROR LINK'), ('ATT_DE3', 'RECHARGE NOMADE'), ('ATT_DE4', 'JUKE BOX'), ('ATT_DPR', 'PROJECTEUR ANTI-BROUILLARD'), ('ATT_DQK', 'AIDE VISUELLE PANORAMIQUE'), ('ATT_DQP', 'AFFICHAGE COMPL DETECTION EXT'), ('ATT_DUB', 'DETECTION OBSTACLE'), ('ATT_DUE', 'DETECTION SOUS GONFLAGE'), ('ATT_DUF', 'SYSTEME ESP/ESC'), ('ATT_DYC', 'STOP AND START'), ('ATT_DYQ', 'ALLUMAGE FEUX'), ('ATT_DZE', 'PACK VISION'), ('ELE_14R', 'AAS HARD - Aide Au Stationnement')], max_length=100, verbose_name='colonne'),
        ),
    ]
