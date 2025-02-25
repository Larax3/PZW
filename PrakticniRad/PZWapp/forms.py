from django import forms
from django.core.exceptions import ValidationError
from .models import Korisnik,VrtnaBiljka

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Lozinka', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Ponovi lozinku', widget=forms.PasswordInput)

    class Meta:
        model = Korisnik
        fields = ['ime', 'prezime', 'username', 'email', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Lozinke se ne podudaraju.')
        return cd['password2']

    def save(self, commit=True):
        korisnik = super().save(commit=False)
        korisnik.set_password(self.cleaned_data['password'])
        if commit:
            korisnik.save()
        return korisnik

class VrtnaBiljkaForm(forms.ModelForm):
    class Meta:
        model = VrtnaBiljka
        fields = ['ime_v', 'regijaBiljke_v', 'vrijemeSazrijevanja_v']  # Polja iz modela

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Dohvati korisnika ako je proslijeđen
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user  # Automatski postavi user polje
