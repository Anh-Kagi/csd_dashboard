# Generated by Django 3.2.13 on 2022-06-28 06:55

from django.db import migrations, models
import squalaetp.models


class Migration(migrations.Migration):

    dependencies = [
        ('squalaetp', '0043_xelontemporary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xelontemporary',
            name='end_date',
            field=models.DateField(blank=True, default=squalaetp.models.get_deadline, null=True, verbose_name='date de fin'),
        ),
    ]