# Generated by Django 3.2.8 on 2022-01-06 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volvo', '0001_initial'),
        ('reman', '0019_repair_recovery'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='brand',
            field=models.CharField(default='PSA', max_length=50, verbose_name='marque'),
        ),
        migrations.AddField(
            model_name='batch',
            name='sem_ref_base',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='volvo.semrefbase'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='ecu_ref_base',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reman.ecurefbase'),
        ),
    ]
