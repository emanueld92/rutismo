from django.db import models

# Create your models here.
class Nino(models.Model):
    
    MASCULINO="H"
    FEMENINO="F"
    
    GENERO_CHOICES=[
        ( MASCULINO, 'Masculino'),
        ( FEMENINO, 'Femenino'),
       
    ]
    
    date = models.DateField('Date', auto_now=False, auto_now_add=False)
    reloj = models.CharField('Reloj', max_length=100)
    cedula = models.CharField('C.I', max_length=50, null=True ,blank=True)
    nombre = models.CharField('Nombre', max_length=100)
    f_nac = models.DateField("Fecha de Nacimiento", auto_now=False, auto_now_add=False)
    genero = models.CharField("genero", max_length=50, choices=GENERO_CHOICES)
    

    
    class Meta:
        """Meta definition for Nino."""

        verbose_name = 'Nino'
        verbose_name_plural = 'Ninos'

class Bitacora(models.Model):
    """Model definition for Bitacora."""

    fecha = models.DateField("Fecha", auto_now=False, auto_now_add=False)
    hora = models.CharField("Hora", max_length=50)
    nombre_rutina = models.CharField("Nombre", max_length=100)
    tipo = models.CharField("tipo", max_length=50)

    class Meta:
        """Meta definition for Bitacora."""

        verbose_name = 'Bitacora'
        verbose_name_plural = 'Bitacoras'

class Rutina(models.Model):
    """Model definition for Rutina."""

    date = models.DateField("date", auto_now=False, auto_now_add=False)
    reloj = models.DateField("reloj", auto_now=False, auto_now_add=False)
    codigo = models.CharField("codigo", max_length=20)
    nombre = models.CharField("nombre", max_length=100)
    turno = models.CharField("turno", max_length=50)
    hota = models.CharField("hora", max_length=50)
    id_nino=models.ManyToManyField(Nino)

    class Meta:
        """Meta definition for Rutina."""

        verbose_name = 'Rutina'
        verbose_name_plural = 'Rutinas'

