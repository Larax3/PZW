from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import VrtnaBiljka, PovrtnaBiljka, Korisnik
from django.urls import reverse_lazy
from .forms import UserRegistrationForm,VrtnaBiljkaForm, PovrtnaBiljkaForm
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('PZWapp:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
    
    return render(request, 'registration/register.html', {'form': form})

def custom_logout(request):
    print("Pozvan je logout!")
    logout(request)
    return redirect('login')

def admin_view(request):
    korisnici = Korisnik.objects.all()
    return render(request, 'main/admin_views.html', {'korisnik': request.user, 'korisnici': korisnici})

def delete_user(request, user_id):
    korisnik = get_object_or_404(Korisnik, id=user_id)
    korisnik.delete()
    return redirect('PZWapp:admin_view')


@login_required
def homepage(request):
    return render(request, 'main/homepage.html', {'korisnik': request.user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        korisnik = authenticate(request, username=username, password=password)
        
        if korisnik is not None:
            login(request, korisnik)
            return redirect('PZWapp:homepage')
        else:
            return render(request, 'registration/login.html', {'error': 'Neispravno korisničko ime ili lozinka'})

    return render(request, 'registration/login.html')


class VrtnaBiljkaListView(LoginRequiredMixin, ListView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_list.html'
    context_object_name = 'biljke'
    def get_queryset(self):
        return VrtnaBiljka.objects.filter(user=self.request.user).exclude(user__isnull=True)


class VrtnaBiljkaDetailView(DetailView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_sazrijevanje_context(self.object.vrijemeSazrijevanja_v))
        return context

    def get_sazrijevanje_context(self, vrijeme_sazrijevanja):
        months = ["Siječanj", "Veljača", "Ožujak", "Travanj", "Svibanj", "Lipanj",
                "Srpanj", "Kolovoz", "Rujan", "Listopad", "Studeni", "Prosinac"]

        highlighted_months = []

        if vrijeme_sazrijevanja:
            try:
            # Očisti nepotrebne razmake i podijeli po " - "
                start_month, end_month = [m.strip() for m in vrijeme_sazrijevanja.split("-")]

                # Dohvati indekse mjeseci
                start_index = months.index(start_month)
                end_index = months.index(end_month)

                # Istakni mjesece u rasponu
                highlighted_months = [months[i] for i in range(start_index, end_index + 1)]
            except ValueError:
                print("Greška kod prepoznavanja mjeseci:", vrijeme_sazrijevanja)

        return {'months': months, 'highlighted_months': highlighted_months}


class VrtnaBiljkaCreateView(LoginRequiredMixin, CreateView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_form.html'
    form_class = VrtnaBiljkaForm
    success_url = reverse_lazy('PZWapp:vrtnabiljka_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Prosljeđuje korisnika u formu kako bi se filtrirale biljke"""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class VrtnaBiljkaUpdateView(LoginRequiredMixin, UpdateView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_form.html'
    fields = ['ime_v', 'regijaBiljke_v', 'vrijemeSazrijevanja_v']
    template_name = 'main/vrtna_biljka_update.html'
    success_url = reverse_lazy('PZWapp:vrtnabiljka_list')

class VrtnaBiljkaDeleteView(LoginRequiredMixin, DeleteView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_confirm_delete.html'
    success_url = reverse_lazy('PZWapp:vrtnabiljka_list')

class PovrtnaBiljkaListView(LoginRequiredMixin, ListView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_list.html'
    context_object_name = 'biljke' 

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return PovrtnaBiljka.objects.filter(user_id=self.request.user.id).exclude(user__isnull=True)
        else:
            return PovrtnaBiljka.objects.none()

class PovrtnaBiljkaCreateView(LoginRequiredMixin, CreateView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_form.html'
    form_class = PovrtnaBiljkaForm
    success_url = reverse_lazy('PZWapp:povrtnabiljka_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Prosljeđuje korisnika u formu kako bi se filtrirale biljke"""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PovrtnaBiljkaUpdateView(LoginRequiredMixin, UpdateView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_form.html'
    fields = ['ime_p', 'regijaBiljke_p', 'vrijemeSazrijevanja_p']
    template_name = 'main/povrtna_biljka_update.html'
    success_url = reverse_lazy('PZWapp:povrtnabiljka_list')

class PovrtnaBiljkaDeleteView(LoginRequiredMixin, DeleteView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_confirm_delete.html'
    success_url = reverse_lazy('PZWapp:povrtnabiljka_list')
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return PovrtnaBiljka.objects.filter(user=self.request.user)
        return PovrtnaBiljka.objects.none()

class PovrtnaBiljkaDetailView(DetailView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_sazrijevanje_context(self.object.vrijemeSazrijevanja_p))
        return context

    def get_sazrijevanje_context(self, vrijeme_sazrijevanja):
        months = ["Siječanj", "Veljača", "Ožujak", "Travanj", "Svibanj", "Lipanj",
                "Srpanj", "Kolovoz", "Rujan", "Listopad", "Studeni", "Prosinac"]

        highlighted_months = []

        if vrijeme_sazrijevanja:
            try:
            # Očisti nepotrebne razmake i podijeli po " - "
                start_month, end_month = [m.strip() for m in vrijeme_sazrijevanja.split("-")]

                # Dohvati indekse mjeseci
                start_index = months.index(start_month)
                end_index = months.index(end_month)

                # Istakni mjesece u rasponu
                highlighted_months = [months[i] for i in range(start_index, end_index + 1)]
            except ValueError:
                print("Greška kod prepoznavanja mjeseci:", vrijeme_sazrijevanja)

        return {'months': months, 'highlighted_months': highlighted_months}
