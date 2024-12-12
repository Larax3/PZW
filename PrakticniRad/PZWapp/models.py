from django.db import models

class VrtnaBiljka(models.Model):
    ime_v = models.CharField(max_length = 30)
    slikaBiljke_v = models.ImageField()
    regijaBiljke_v = models.CharField(max_length = 20)
    vrijemeSazrijevanja_v = models.CharField(max_length = 15)
    


class PovrtnaBiljka(models.Model):
    ime_p = models.CharField(max_length = 30)
    slikaBiljke_p = models.ImageField()
    regijaBiljke_p = models.CharField(max_length = 20)
    vrijemeSazrijevanja_p = models.CharField(max_length = 15)

