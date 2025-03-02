from django.contrib import admin
from .models import VrtnaBiljka, PovrtnaBiljka, Korisnik

admin.site.register(VrtnaBiljka)
admin.site.register(PovrtnaBiljka)
admin.site.register(Korisnik)
