# Generated by Django 3.0.2 on 2020-01-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squalaetp', '0015_auto_20191124_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corvet',
            name='donnee_date_debut_garantie',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date d?but garantie'),
        ),
        migrations.AlterField(
            model_name='corvet',
            name='donnee_date_entree_montage',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date entr?e montage'),
        ),
    ]