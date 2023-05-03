from django.contrib import admin

from .models import Voiture, Garage, Utilisateur

# Register your models here.

admin.site.register([
    Voiture, Garage, Utilisateur
])
