# Generated by Django 3.2.11 on 2022-01-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squalaetp', '0036_productcategory_corvet_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='xelon',
            name='date_expedition_attendue',
            field=models.DateField(blank=True, null=True, verbose_name='date expédition attendue'),
        ),
        migrations.AddField(
            model_name='xelon',
            name='delai_expedition_attendue',
            field=models.IntegerField(blank=True, null=True, verbose_name='délai expédition attendue'),
        ),
    ]
