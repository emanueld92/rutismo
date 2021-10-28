from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField


# Create your models here.
class Nino(models.Model):
    MASCULINO = "M"
    FEMENINO = "F"

    GENEROS = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    ]
    """Model definition for nino."""

    # TODO: Define fields here
    update = models.DateField("update", auto_now=True, auto_now_add=True)
    nombre = models.CharField("nombre", max_length=50)
    cedula = models.CharField("cedula", max_length=50, null=True, blank=True)
    f_nacimiento = models.DateField(
        "Fecha de nacimiento", auto_now=False, auto_now_add=False)
    genero = models.CharField("genero", max_length=50,
                              choices=GENEROS, default=MASCULINO)


class Rutina(models.Model):
    MANANA = "AM"
    TARDE = "PM"

    TURNO = [
        (MANANA, "MAÑANA"),
        (TARDE, "TARDE"),
    ]

    fecha = models.DateField("fecha", auto_now=True, auto_now_add=True)
    codigo = models.CharField("codigo", max_length=50)
    nombre_rutina = models.CharField("Nombre Rutina", max_length=50)
    turno = models.CharField("Turno", max_length=50,
                             choices=TURNO, default=MANANA)
    id_nino = ManyToManyField(Nino)


class Bitacora(models.Model):
    """Model definition for bitacora."""

    # TODO: Define fields here
    fecha = models.DateField("Fecha", auto_now=False, auto_now_add=False)
    nombre_rutina = models.CharField("Nombre de la Rutina", max_length=100)
    tipo = models.CharField("Tipo", max_length=50)
