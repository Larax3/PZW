from django.core.management.base import BaseCommand
from PZWapp.models import VrtnaBiljka, PovrtnaBiljka, Korisnik  # Use your custom user model

class Command(BaseCommand):
    help = "Dodaje testne vrtne i povrtne biljke u bazu podataka za korisnika 'rino'"

    def handle(self, *args, **kwargs):
        # Get user from custom user model (Korisnik)
        try:
            user = Korisnik.objects.get(username="rino")  # Use Korisnik instead of User
        except Korisnik.DoesNotExist:
            self.stdout.write(self.style.ERROR("Korisnik 'rino' ne postoji! Kreiraj ga prije pokretanja ove skripte."))
            return

        vrtne_biljke = [
            {"ime_v": "Lavanda", "regijaBiljke_v": "Mediteran", "vrijemeSazrijevanja_v": "Ožujak - Svibanj"},
            {"ime_v": "Ružmarin", "regijaBiljke_v": "Mediteran", "vrijemeSazrijevanja_v": "Travanj - Lipanj"},
            {"ime_v": "Bosiljak", "regijaBiljke_v": "Topli krajevi", "vrijemeSazrijevanja_v": "Lipanj - Kolovoz"},
            {"ime_v": "Kadulja", "regijaBiljke_v": "Sredozemlje", "vrijemeSazrijevanja_v": "Svibanj - Rujan"},
            {"ime_v": "Majčina dušica", "regijaBiljke_v": "Planinski krajevi", "vrijemeSazrijevanja_v": "Travanj - Kolovoz"},
            {"ime_v": "Menta", "regijaBiljke_v": "Umjerena klima", "vrijemeSazrijevanja_v": "Svibanj - Kolovoz"},
            {"ime_v": "Peršin", "regijaBiljke_v": "Umjerena klima", "vrijemeSazrijevanja_v": "Ožujak - Listopad"},
            {"ime_v": "Timijan", "regijaBiljke_v": "Mediteran", "vrijemeSazrijevanja_v": "Travanj - Kolovoz"},
            {"ime_v": "Matricaria", "regijaBiljke_v": "Planinski krajevi", "vrijemeSazrijevanja_v": "Svibanj - Rujan"},
            {"ime_v": "Neven", "regijaBiljke_v": "Srednja Europa", "vrijemeSazrijevanja_v": "Svibanj - Kolovoz"}
        ]

        povrtne_biljke = [
            {"ime_p": "Rajčica", "regijaBiljke_p": "Topli krajevi", "vrijemeSazrijevanja_p": "Lipanj - Kolovoz"},
            {"ime_p": "Paprika", "regijaBiljke_p": "Topli krajevi", "vrijemeSazrijevanja_p": "Lipanj - Rujan"},
            {"ime_p": "Krastavac", "regijaBiljke_p": "Umjerena klima", "vrijemeSazrijevanja_p": "Svibanj - Kolovoz"},
            {"ime_p": "Mrkva", "regijaBiljke_p": "Srednja Europa", "vrijemeSazrijevanja_p": "Travanj - Listopad"},
            {"ime_p": "Luk", "regijaBiljke_p": "Umjerena klima", "vrijemeSazrijevanja_p": "Ožujak - Srpanj"},
            {"ime_p": "Češnjak", "regijaBiljke_p": "Sredozemlje", "vrijemeSazrijevanja_p": "Ožujak - Lipanj"},
            {"ime_p": "Špinat", "regijaBiljke_p": "Hladnije klime", "vrijemeSazrijevanja_p": "Ožujak - Listopad"},
            {"ime_p": "Grah", "regijaBiljke_p": "Umjerena klima", "vrijemeSazrijevanja_p": "Svibanj - Rujan"},
            {"ime_p": "Tikvica", "regijaBiljke_p": "Topli krajevi", "vrijemeSazrijevanja_p": "Lipanj - Rujan"},
            {"ime_p": "Kelj", "regijaBiljke_p": "Hladnije klime", "vrijemeSazrijevanja_p": "Kolovoz - Prosinac"}
        ]

        # Add vrtne biljke
        for biljka in vrtne_biljke:
            biljka_obj, created = VrtnaBiljka.objects.get_or_create(user=user, **biljka)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Vrtna biljka '{biljka['ime_v']}' dodana korisniku 'rino'."))
            else:
                self.stdout.write(self.style.WARNING(f"Vrtna biljka '{biljka['ime_v']}' već postoji za korisnika 'rino'."))

        # Add povrtne biljke
        for biljka in povrtne_biljke:
            biljka_obj, created = PovrtnaBiljka.objects.get_or_create(user=user, **biljka)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Povrtna biljka '{biljka['ime_p']}' dodana korisniku 'rino'."))
            else:
                self.stdout.write(self.style.WARNING(f"Povrtna biljka '{biljka['ime_p']}' već postoji za korisnika 'rino'."))

        self.stdout.write(self.style.SUCCESS("Uspješno dodane vrtne i povrtne biljke korisniku 'rino' u bazu."))
