# Generated by Django 3.2.6 on 2022-03-22 06:39

import apps.ruta.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0004_alter_nino_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nino',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=apps.ruta.models.path_avatar, verbose_name='foto'),
        ),
    ]
