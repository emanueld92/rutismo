
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


def path_avatar(instance, filename):
    return f'avatars/{instance.first_name}/{filename}'


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(
        'Avatar', upload_to=path_avatar,blank=True, null=True)
    first_name=models.CharField(blank=True, max_length=150, verbose_name='Nombre')
    last_name=models.CharField(blank=True, max_length=150, verbose_name='Apellido')
 
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

  
  
  
  
  
