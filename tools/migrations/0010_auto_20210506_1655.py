# Generated by Django 3.2 on 2021-05-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0009_auto_20210316_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='suptech',
            name='deadline',
            field=models.DateField(null=True, verbose_name='DATE LIMITE'),
        ),
        migrations.AddField(
            model_name='suptech',
            name='status',
            field=models.TextField(choices=[('En Attente', 'En Attente'), ('En Cours', 'En Cours'), ('Cloturée', 'Cloturée'), ('Annulée', 'Annulée')], default='En Attente', max_length=50, verbose_name='STATUT'),
        ),
    ]
