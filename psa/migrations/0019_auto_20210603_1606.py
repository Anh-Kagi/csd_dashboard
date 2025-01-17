# Generated by Django 3.2.3 on 2021-06-03 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psa', '0018_delete_emfmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corvet',
            name='bsi',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'BSI'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='psa.ecu'),
        ),
        migrations.AlterField(
            model_name='corvet',
            name='bsm',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'BSM'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='psa.ecu'),
        ),
        migrations.AlterField(
            model_name='corvet',
            name='btel',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'NAV'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='psa.multimedia'),
        ),
        migrations.AlterField(
            model_name='corvet',
            name='cmm',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'CMM'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='psa.ecu'),
        ),
        migrations.AlterField(
            model_name='corvet',
            name='emf',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'EMF'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='psa.ecu'),
        ),
        migrations.AlterField(
            model_name='corvet',
            name='radio',
            field=models.ForeignKey(blank=True, limit_choices_to={'type': 'RAD'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='psa.multimedia'),
        ),
        migrations.CreateModel(
            name='CorvetProduct',
            fields=[
                ('corvet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='prods', serialize=False, to='psa.corvet')),
                ('bsi', models.ForeignKey(blank=True, limit_choices_to={'type': 'BSI'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corvet_bsi', to='psa.ecu')),
                ('bsm', models.ForeignKey(blank=True, limit_choices_to={'type': 'BSM'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corvet_bsm', to='psa.ecu')),
                ('btel', models.ForeignKey(blank=True, limit_choices_to={'type': 'NAV'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corvet_btel', to='psa.multimedia')),
                ('cmm', models.ForeignKey(blank=True, limit_choices_to={'type': 'CMM'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corvet_cmm', to='psa.ecu')),
                ('emf', models.ForeignKey(blank=True, limit_choices_to={'type': 'EMF'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corvet_emf', to='psa.ecu')),
                ('hdc', models.ForeignKey(blank=True, limit_choices_to={'type': 'HDC'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corvet_hdc', to='psa.ecu')),
                ('radio', models.ForeignKey(blank=True, limit_choices_to={'type': 'RAD'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corvet_radio', to='psa.multimedia')),
            ],
            options={
                'verbose_name': 'produits CORVET',
                'ordering': ['corvet'],
            },
        ),
    ]
