# Generated by Django 3.0.4 on 2020-04-03 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_delete_csdsoftware'),
        ('squalaetp', '0016_auto_20200113_1012'),
        ('raspeedi', '0009_auto_20200323_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='unlockproduct',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='unlockproduct',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='modifié le'),
        ),
        migrations.AlterField(
            model_name='unlockproduct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ajouté le'),
        ),
        migrations.AlterField(
            model_name='unlockproduct',
            name='unlock',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='squalaetp.Xelon'),
        ),
        migrations.AlterField(
            model_name='unlockproduct',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='dashboard.UserProfile'),
        ),
    ]