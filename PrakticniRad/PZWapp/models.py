from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

def get_default_user():
    User = get_user_model()
    user = User.objects.get(username='admin')
    return user.id  

class Korisnik(AbstractUser):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.ime} {self.prezime}"

class VrtnaBiljka(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='vrtne_biljke',
        default=get_default_user()
    )
    ime_v = models.CharField(max_length=30)
    regijaBiljke_v = models.CharField(max_length=100)
    vrijemeSazrijevanja_v = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ime_v} ({self.user.username})"

class PovrtnaBiljka(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='povrtne_biljke',
        default=get_default_user()
    )
    ime_p = models.CharField(max_length=30)
    regijaBiljke_p = models.CharField(max_length=100)
    vrijemeSazrijevanja_p = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ime_p} ({self.user.username})"
