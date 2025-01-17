# Generated by Django 3.2.11 on 2022-01-18 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volvo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asm_reference', models.CharField(max_length=12, unique=True, verbose_name='ASM')),
                ('hw_reference', models.CharField(max_length=12, verbose_name='HW')),
                ('technical_data', models.CharField(default='SEM', max_length=50, verbose_name='modèle produit')),
                ('supplier_oe', models.CharField(default='PARROT', max_length=50, verbose_name='fabriquant')),
            ],
        ),
        migrations.RenameField(
            model_name='semrefbase',
            old_name='oe_reference',
            new_name='product_part',
        ),
        migrations.RemoveField(
            model_name='semrefbase',
            name='asm',
        ),
        migrations.RemoveField(
            model_name='semrefbase',
            name='hw',
        ),
        migrations.AddField(
            model_name='semrefbase',
            name='brand',
            field=models.CharField(blank=True, max_length=50, verbose_name='Marque'),
        ),
        migrations.AlterField(
            model_name='semrefbase',
            name='pf_code',
            field=models.CharField(blank=True, max_length=10, verbose_name='PF code REMAN'),
        ),
        migrations.CreateModel(
            name='SemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_code_oe', models.CharField(max_length=10, unique=True, verbose_name='PF code OE')),
                ('pi_code_oe', models.CharField(max_length=10, verbose_name='PI code OE')),
                ('sam_oe', models.CharField(blank=True, max_length=12, verbose_name='Production part')),
                ('vehicle', models.CharField(blank=True, max_length=50, verbose_name='Vehicule')),
                ('core_part', models.CharField(blank=True, max_length=50, verbose_name='Core part')),
                ('fan', models.CharField(blank=True, max_length=100, verbose_name='FAN')),
                ('rear_bolt', models.CharField(blank=True, max_length=100, verbose_name='REAR BOLT')),
                ('hw_oe', models.CharField(blank=True, max_length=12, verbose_name='HW P/N')),
                ('ecu_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='volvo.semtype')),
            ],
        ),
        migrations.AddField(
            model_name='semrefbase',
            name='ecu_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='volvo.semtype'),
        ),
    ]
