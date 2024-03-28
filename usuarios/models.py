from django.db import models
from django.contrib.auth.models import AbstractUser #importa classe user da padrão do django
# Create your models here.


class Users(AbstractUser):
    choices_cargo = (('R','RH'),
                     ('A','Avaliador'))
    cargo = models.CharField(max_length=1, choices=choices_cargo)