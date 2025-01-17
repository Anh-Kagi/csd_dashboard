# Generated by Django 3.2.7 on 2021-09-22 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0016_suptechmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuptechCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nom')),
            ],
        ),
        migrations.AddField(
            model_name='suptech',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.suptechcategory'),
        ),
        migrations.AddField(
            model_name='suptechitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.suptechcategory'),
        ),
    ]
