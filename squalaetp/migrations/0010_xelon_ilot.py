# Generated by Django 2.2.4 on 2019-08-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squalaetp', '0009_auto_20190828_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='xelon',
            name='ilot',
            field=models.CharField(blank=True, max_length=100, verbose_name='ilot'),
        ),
    ]