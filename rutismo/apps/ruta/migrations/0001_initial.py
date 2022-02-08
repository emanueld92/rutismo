# Generated by Django 3.2.6 on 2021-11-13 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id_bitacora', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha')),
                ('nombre_bitacora', models.CharField(max_length=100, verbose_name='Nombre')),
                ('e_animo', models.CharField(choices=[('CO', 'CONTENTO'), ('TR', 'TRISTE'), ('EF', 'ENFERMO')], default='CO', max_length=20, verbose_name='Estado de Animo')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='MApoyo',
            fields=[
                ('id_mapoyo', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(choices=[('AL', 'ALIMENTACION'), ('AS', 'ASEO PERSONAL'), ('OC', 'OCIO'), ('TD', 'TAREAS DOMESTICAS'), ('OT', 'OTROS')], max_length=20, verbose_name='Categoria')),
                ('imagen', models.ImageField(upload_to='Mapoyo', verbose_name='imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Nino',
            fields=[
                ('id_nino', models.AutoField(primary_key=True, serialize=False)),
                ('update', models.DateField(auto_now_add=True, verbose_name='update')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('cedula', models.CharField(blank=True, max_length=50, null=True, verbose_name='cedula')),
                ('f_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=50, verbose_name='genero')),
                ('foto', models.ImageField(upload_to='ninos', verbose_name='foto')),
            ],
        ),
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id_rutina', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now=True, verbose_name='fecha')),
                ('codigo', models.CharField(max_length=50, verbose_name='codigo')),
                ('nombre_rutina', models.CharField(max_length=50, verbose_name='Nombre Rutina')),
                ('turno', models.CharField(choices=[('AM', 'MAÑANA'), ('PM', 'TARDE')], default='AM', max_length=50, verbose_name='Turno')),
                ('id_mapoyo', models.ManyToManyField(to='ruta.MApoyo')),
                ('id_nino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruta.nino')),
            ],
        ),
    ]
