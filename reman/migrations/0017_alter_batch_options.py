# Generated by Django 3.2.4 on 2021-07-01 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reman', '0016_auto_20210629_1252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'permissions': [('pdfgen_batch', 'Can pdfgen batch')]},
        ),
    ]