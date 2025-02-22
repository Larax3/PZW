from django import forms
from .models import Korisnik

class RegisterForm(forms.ModelForm):
    lozinka = forms.CharField(widget=forms.PasswordInput) 

    class Meta:
        model = Korisnik
        fields = ['ime', 'prezime', 'email', 'username', 'lozinka']  