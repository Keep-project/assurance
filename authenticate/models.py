from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Utilisateur(AbstractUser):
    telephone = models.CharField(max_length=200)
    avatar = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Utilisateur'


class Voiture(models.Model):
    name = models.CharField(max_length=200)


class Garage(models.Model):
    name = models.CharField(max_length=200)