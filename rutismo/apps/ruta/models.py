from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField

from rutismo.settings.base import BASE_DIR
from ..usuarios.models import CustomUser
import os
# Create your models here.


def path_avatar(instance, filename):
    return f'ninos/{instance.nombre}/{filename}'


class Nino(models.Model):
    MASCULINO = "M"
    FEMENINO = "F"

    GENEROS = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    ]
    """Model definition for nino."""

    # TODO: Define fields here
    id_nino = models.AutoField(primary_key=True)
    update = models.DateField("update", auto_now=False, auto_now_add=True)
    nombre = models.CharField("nombre", max_length=50)
    f_nacimiento = models.DateField(
        "Fecha de nacimiento", auto_now=False, auto_now_add=False)
    genero = models.CharField("genero", max_length=50,
                              choices=GENEROS, default=MASCULINO)
    foto = models.ImageField(
        "foto", upload_to=path_avatar, blank=True, null=True)
    adulto = models.ForeignKey(CustomUser, on_delete=CASCADE,)


class MApoyo(models.Model):

    ALIMENTACION = "AL"
    ASEO_PERSONAL = "AS"
    OCIO = "OC"
    TAREAS_DOMESTICAS = "TD"
    OTROS = "OT"

    CATEGORIA = [
        (ALIMENTACION, 'ALIMENTACION'),
        (ASEO_PERSONAL, 'ASEO PERSONAL'),
        (OCIO, 'OCIO'),
        (TAREAS_DOMESTICAS, 'TAREAS DOMESTICAS'),
        (OTROS, 'OTROS'),
    ]

    id_mapoyo = models.AutoField(primary_key=True)
    categoria = models.CharField("Categoria", max_length=20, choices=CATEGORIA)
    imagen = models.ImageField('imagen', upload_to='Mapoyo',
                               height_field=None, width_field=None, max_length=None)


class Rutina(models.Model):
    MANANA = "AM"
    TARDE = "PM"

    TURNO = [
        (MANANA, "MAÑANA"),
        (TARDE, "TARDE"),
    ]
    id_rutina = models.AutoField(primary_key=True)
    fecha = models.DateField("fecha", auto_now=True, auto_now_add=False)
    codigo = models.CharField("codigo", max_length=50)
    nombre_rutina = models.CharField("Nombre Rutina", max_length=50)
    turno = models.CharField("Turno", max_length=50,
                             choices=TURNO, default=MANANA)
    id_nino = models.ForeignKey(Nino, on_delete=models.CASCADE)
    id_mapoyo = models.ManyToManyField(MApoyo)


class Bitacora(models.Model):
    """Model definition for bitacora."""

    CONTENTO = "CONTENTO"
    TRISTE = "TRISTE"
    ENFERMO = "ENFERMO"

    ANIMO = [
        (CONTENTO, "CONTENTO"),
        (TRISTE, "TRISTE"),
        (ENFERMO, "ENFERMO"),
    ]

    # TODO: Define fields here
    id_bitacora = models.AutoField(primary_key=True)
    fecha = models.DateTimeField("Fecha", auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(CustomUser, on_delete=CASCADE,)
    e_animo = models.CharField(
        "Estado de Animo", max_length=20, choices=ANIMO, default=CONTENTO)
