from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.contrib.auth.models import AbstractUser

def get_default_user():
    return Korisnik.objects.get(username='rino').id

class VrtnaBiljka(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='vrtne_biljke',
        default=get_default_user
    )
    ime_v = models.CharField(max_length=30)
    slikaBiljke_v = models.ImageField(upload_to='images/', blank=True, null=True)
    regijaBiljke_v = models.CharField(max_length=20)
    vrijemeSazrijevanja_v = models.CharField(max_length=15)

    def __str__(self):
        return self.ime_v

class PovrtnaBiljka(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='povrtne_biljke',
        default=get_default_user
    )
    ime_p = models.CharField(max_length=30)
    slikaBiljke_p = models.ImageField(upload_to='images/', blank=True, null=True)
    regijaBiljke_p = models.CharField(max_length=20)
    vrijemeSazrijevanja_p = models.CharField(max_length=15)

    def __str__(self):
        return self.ime_p

class Korisnik(AbstractUser):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True, default="rino")

    def __str__(self):
        return f"{self.ime} {self.prezime}"

