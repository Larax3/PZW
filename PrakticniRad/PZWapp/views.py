from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import VrtnaBiljka, PovrtnaBiljka, Korisnik
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.hashers import check_password


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            korisnik = form.save(commit=False)  
            korisnik.set_password(form.cleaned_data['lozinka']) 
            korisnik.save() 
            return redirect('PZWapp:login')  
    else:
        form = RegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})
def custom_logout(request):
    logout(request)
    return redirect('login')

def admin_view(request):
    # Dohvati sve korisnike
    korisnici = Korisnik.objects.all()
    context = {
        'korisnici': korisnici
    }
    return render(request, 'main/admin_views.html', context)

def delete_user(request, user_id):
    korisnik = get_object_or_404(Korisnik, id=user_id)
    korisnik.delete()
    return redirect('PZWapp:admin_view')

def homepage(request):
    korisnik_id = request.session.get('korisnik_id')
    if korisnik_id:
        korisnik = Korisnik.objects.get(id=korisnik_id)
        return render(request, 'main/homepage.html', {'korisnik': korisnik})
    else:
        return redirect('PZWapp:login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            korisnik = Korisnik.objects.get(username=username)
            if check_password(password, korisnik.lozinka):  
        
                return redirect('PZWapp:homepage')
            else:
                
                return render(request, 'registration/login.html', {'error': 'Neispravno korisničko ime ili lozinka'})
        except Korisnik.DoesNotExist:
           
            return render(request, 'registration/login.html', {'error': 'Neispravno korisničko ime ili lozinka'})
    else:
        return render(request, 'registration/login.html')

class VrtnaBiljkaListView(ListView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_list.html'
    context_object_name = 'biljke'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return VrtnaBiljka.objects.filter(ime_v__icontains=query)
        return VrtnaBiljka.objects.all()

class PovrtnaBiljkaListView(ListView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_list.html'
    context_object_name = 'biljke'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return PovrtnaBiljka.objects.filter(ime_p__icontains=query)
        return PovrtnaBiljka.objects.all()

class VrtnaBiljkaDetailView(DetailView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_detail.html'

class PovrtnaBiljkaDetailView(DetailView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_detail.html'

def kreiraj_testne_podatke(request):
    # Kreiranje testnih podataka
    VrtnaBiljka.objects.bulk_create([
        VrtnaBiljka(ime_v='Ruža', regijaBiljke_v='Mediteran', vrijemeSazrijevanja_v='Proljeće'),
        VrtnaBiljka(ime_v='Lala', regijaBiljke_v='Balkan', vrijemeSazrijevanja_v='Proljeće'),
    ])

    PovrtnaBiljka.objects.bulk_create([
        PovrtnaBiljka(ime_p='Mrkva', regijaBiljke_p='Kontinentalna', vrijemeSazrijevanja_p='Ljeto'),
        PovrtnaBiljka(ime_p='Krumpir', regijaBiljke_p='Planinska', vrijemeSazrijevanja_p='Ljeto'),
    ])

    return HttpResponse("Testni podaci su uspješno kreirani!")

class VrtnaBiljkaCreateView(CreateView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_form.html'
    fields = ['ime_v', 'slikaBiljke_v', 'regijaBiljke_v', 'vrijemeSazrijevanja_v']
    success_url = reverse_lazy('PZWapp:vrtnabiljka_list')

class VrtnaBiljkaUpdateView(UpdateView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_form.html'
    fields = ['ime_v', 'slikaBiljke_v', 'regijaBiljke_v', 'vrijemeSazrijevanja_v']
    success_url = reverse_lazy('PZWapp:vrtnabiljka_list')

class VrtnaBiljkaDeleteView(DeleteView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_confirm_delete.html'
    success_url = reverse_lazy('PZWapp:vrtnabiljka_list')

class PovrtnaBiljkaCreateView(CreateView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_form.html'
    fields = ['ime_p', 'slikaBiljke_p', 'regijaBiljke_p', 'vrijemeSazrijevanja_p']
    success_url = reverse_lazy('PZWapp:povrtnabiljka_list')

class PovrtnaBiljkaUpdateView(UpdateView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_form.html'
    fields = ['ime_p', 'slikaBiljke_p', 'regijaBiljke_p', 'vrijemeSazrijevanja_p']
    success_url = reverse_lazy('PZWapp:povrtnabiljka_list')

class PovrtnaBiljkaDeleteView(DeleteView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_confirm_delete.html'
    success_url = reverse_lazy('PZWapp:povrtnabiljka_list')
