# Generated by Django 3.2.3 on 2021-05-14 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squalaetp', '0029_productcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='xelon',
            options={'ordering': ['numero_de_dossier'], 'permissions': [('change_product', 'Can change product'), ('email_product', 'Can send email product'), ('change_vin', 'Can change vin'), ('email_vin', 'Can send email vin'), ('active_xelon', 'Can active xelon')], 'verbose_name': 'dossier Xelon'},
        ),
    ]