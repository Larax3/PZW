from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class VrtnaBiljka(models.Model):
    ime_v = models.CharField(max_length=30)
    slikaBiljke_v = models.ImageField(upload_to='images/', blank=True, null=True)
    regijaBiljke_v = models.CharField(max_length=20)
    vrijemeSazrijevanja_v = models.CharField(max_length=15)

    def __str__(self):
        return self.ime_v

class PovrtnaBiljka(models.Model):
    ime_p = models.CharField(max_length=30)
    slikaBiljke_p = models.ImageField(upload_to='images/', blank=True, null=True)
    regijaBiljke_p = models.CharField(max_length=20)
    vrijemeSazrijevanja_p = models.CharField(max_length=15)

    def __str__(self):
        return self.ime_p

class Korisnik(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True,default="rino")  
    lozinka = models.CharField(max_length=128,default="12345") 

    def set_password(self, raw_password):
        self.lozinka = make_password(raw_password) 

    def check_password(self, raw_password):
        return check_password(raw_password, self.lozinka)  

    def __str__(self):
        return f"{self.ime} {self.prezime}"