# Generated by Django 3.2.6 on 2021-11-15 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0003_auto_20211115_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitacora',
            name='e_animo',
            field=models.CharField(choices=[('CONTENTO', 'CONTENTO'), ('TRISTE', 'TRISTE'), ('ENFERMO', 'ENFERMO')], default='CONTENTO', max_length=20, verbose_name='Estado de Animo'),
        ),
        migrations.AlterField(
            model_name='bitacora',
            name='fecha',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha'),
        ),
    ]
