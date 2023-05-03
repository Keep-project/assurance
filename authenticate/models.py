from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Utilisateur(AbstractUser):
    telephone = models.CharField(max_length=200)
    avatar = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Utilisateur'


class Rapport(models.Model):
    date = models.DateTimeField()
    libelle = models.CharField(max_length=200, null=False)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return f'{self.date} {self.id}' 

class Client(models.Model):


    choices = (
    (0, 'Auto'),
    (1, 'voyage'),
    (2, 'Maladie'),
    (3, 'Tout risque'),
    (4, 'Caution'),
    )
    nom = models.CharField(max_length=200, null=False)
    prenom = models.CharField(max_length=200, null=False)
    adresse = models.CharField(max_length=200, null=False)
    date_naiss = models.DateField()
    tel = models.CharField(default=0, max_length=200)
    typeAssur = models.IntegerField(default=0, choices=choices )
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return f'{self.nom} {self.id}' 
