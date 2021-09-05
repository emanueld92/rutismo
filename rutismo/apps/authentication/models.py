from django.contrib.auth.models import AbstractUser
from django.db import models


def path_avatar(instance, filename):
    return f'avatars/{instance.id}/{filename}'


class CustomUser(AbstractUser):
    
    PROFESOR= "PR"
    ADMINISTRADOR="AD"
    REPRESENTANTE="RP"
    OTRO="OTR"
    
    CARGOS_CHOICES=[
        (PROFESOR, 'Profesor'),
        (ADMINISTRADOR, 'Administrador'),
        (REPRESENTANTE, 'Representante'),
        (OTRO, 'Otro'),
    ]

    email = models.EmailField(
        max_length=150, unique=True)
    cargo = models.CharField('cargo', max_length=50, choices=CARGOS_CHOICES)
    USERNAME_FIELD = 'email'  # new
    REQUIRED_FIELDS = ['username', 'password']  # new
    avatar = models.ImageField(
        'Avatar', upload_to=path_avatar, null=True, blank=True)
