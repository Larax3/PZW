from django import forms
from django.core.exceptions import ValidationError
from .models import Korisnik, VrtnaBiljka, PovrtnaBiljka

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Lozinka', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Ponovi lozinku', widget=forms.PasswordInput)

    class Meta:
        model = Korisnik
        fields = ['ime', 'prezime', 'username', 'email', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise ValidationError('Lozinke se ne podudaraju.')
        return cd.get('password2')

    def save(self, commit=True):
        korisnik = super().save(commit=False)
        korisnik.set_password(self.cleaned_data['password'])
        if commit:
            korisnik.save()
        return korisnik


class VrtnaBiljkaForm(forms.ModelForm):
    ime_v = forms.CharField(
        max_length=100,
        label="Ime biljke",
        widget=forms.TextInput(attrs={'placeholder': 'Upiši ime biljke'})
    )
    regijaBiljke_v = forms.CharField(
        max_length=100,
        label="Regija biljke",
        widget=forms.TextInput(attrs={'placeholder': 'Upiši regiju biljke'})
    )
    vrijemeSazrijevanja_v = forms.CharField(
        max_length=50,
        label="Vrijeme sazrijevanja",
        widget=forms.TextInput(attrs={'placeholder': 'Upiši vrijeme sazrijevanja'})
    )

    class Meta:
        model = VrtnaBiljka
        fields = ['ime_v', 'regijaBiljke_v', 'vrijemeSazrijevanja_v']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) 
        super().__init__(*args, **kwargs)
        if user.is_authenticated:
            self.instance.user = user
        else:
            raise ValueError("Korisnik mora biti prijavljen!")



class PovrtnaBiljkaForm(forms.ModelForm):
    ime_p = forms.CharField(
        max_length=100,
        label="Ime biljke",
        widget=forms.TextInput(attrs={'placeholder': 'Upiši ime biljke'})
    )
    regijaBiljke_p = forms.CharField(
        max_length=100,
        label="Regija biljke",
        widget=forms.TextInput(attrs={'placeholder': 'Upiši regiju biljke'})
    )
    vrijemeSazrijevanja_p = forms.CharField(
        max_length=50,
        label="Vrijeme sazrijevanja",
        widget=forms.TextInput(attrs={'placeholder': 'Upiši vrijeme sazrijevanja'})
    )
    class Meta:
        model = PovrtnaBiljka
        fields = ['ime_p', 'regijaBiljke_p', 'vrijemeSazrijevanja_p']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) 
        super().__init__(*args, **kwargs)
        if user.is_authenticated:
            self.instance.user = user
        else:
            raise ValueError("Korisnik mora biti prijavljen!")
