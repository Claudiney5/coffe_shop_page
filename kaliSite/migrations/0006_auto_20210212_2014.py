# Generated by Django 3.1.6 on 2021-02-12 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaliSite', '0005_auto_20210212_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='estoque',
            field=models.IntegerField(default=0, verbose_name='Qtdade em Estoque'),
        ),
    ]