from django.contrib import admin
from .models import VrtnaBiljka, PovrtnaBiljka, Korisnik, FarmaBiljka,Farma

admin.site.register(VrtnaBiljka)
admin.site.register(PovrtnaBiljka)
admin.site.register(Korisnik)
admin.site.register(Farma)
admin.site.register(FarmaBiljka)