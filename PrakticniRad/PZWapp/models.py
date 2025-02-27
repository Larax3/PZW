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
        default = get_default_user
    )
    ime_v = models.CharField(max_length=30)
    regijaBiljke_v = models.CharField(max_length=100)
    vrijemeSazrijevanja_v = models.CharField(max_length=50)

    def __str__(self):
        return self.ime_v

class PovrtnaBiljka(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='povrtne_biljke',
        default = get_default_user
    )
    ime_p = models.CharField(max_length=30)
    regijaBiljke_p = models.CharField(max_length=100)
    vrijemeSazrijevanja_p = models.CharField(max_length=50)

    def __str__(self):
        return self.ime_p


class Korisnik(AbstractUser):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.ime} {self.prezime}"
class Farma(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='farme'
    )
    naziv = models.CharField(max_length=100)
    lokacija = models.CharField(max_length=200)

    def __str__(self):
        return self.naziv

class FarmaBiljka(models.Model):
    farma = models.ForeignKey(Farma, on_delete=models.CASCADE, related_name='biljke_na_farmi')
    biljka_vrtna = models.ForeignKey(VrtnaBiljka, null=True, blank=True, on_delete=models.CASCADE)
    biljka_povrtna = models.ForeignKey(PovrtnaBiljka, null=True, blank=True, on_delete=models.CASCADE)
    kolicina = models.PositiveIntegerField(default=1)

    def __str__(self):
        biljka = self.biljka_vrtna if self.biljka_vrtna else self.biljka_povrtna
        return f"{biljka.ime_v if biljka else 'Nepoznata biljka'} - {self.farma.naziv} ({self.kolicina})"

