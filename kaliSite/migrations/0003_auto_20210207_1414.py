# Generated by Django 3.1.6 on 2021-02-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaliSite', '0002_client'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produto',
            new_name='Product',
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.IntegerField(verbose_name='Telefone'),
        ),
    ]
