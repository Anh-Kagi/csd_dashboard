# Generated by Django 3.2.12 on 2022-04-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0020_auto_20220412_0907'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suptech',
            options={'ordering': ['pk'], 'verbose_name': 'SupTech'},
        ),
        migrations.AddField(
            model_name='suptech',
            name='cc',
            field=models.TextField(default='test1@test.com; test2@test.com', max_length=5000, verbose_name='CC'),
        ),
        migrations.AddField(
            model_name='suptech',
            name='to',
            field=models.TextField(default='test1@test.com; test2@test.com', max_length=5000, verbose_name='TO'),
        ),
    ]
