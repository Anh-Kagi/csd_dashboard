# Generated by Django 3.1.3 on 2020-12-04 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squalaetp', '0022_xelon_corvet'),
    ]

    operations = [
        migrations.AddField(
            model_name='xelon',
            name='vin_error',
            field=models.BooleanField(default=False, verbose_name='Erreur VIN'),
        ),
    ]