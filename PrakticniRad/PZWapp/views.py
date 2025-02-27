from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import VrtnaBiljka, PovrtnaBiljka, Korisnik, Farma, FarmaBiljka
from django.urls import reverse_lazy
from .forms import UserRegistrationForm,VrtnaBiljkaForm, PovrtnaBiljkaForm,FarmaForm, FarmaBiljkaForm
from django.shortcuts import render, redirect

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
    logout(request)
    return redirect('login')

def admin_view(request):
    korisnici = Korisnik.objects.all()
    context = {
        'korisnici': korisnici
    }
    return render(request, 'main/admin_views.html', context)

def delete_user(request, user_id):
    korisnik = get_object_or_404(Korisnik, id=user_id)
    korisnik.delete()
    return redirect('PZWapp:admin_view')

from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    return render(request, 'main/homepage.html', {'korisnik': request.user})



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
        biljke = VrtnaBiljka.objects.filter(user=self.request.user)  
        if query:
            biljke = biljke.filter(ime_v__icontains=query)
        return biljke

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

        if vrijeme_sazrijevanja:
            try:
                start_month, end_month = vrijeme_sazrijevanja.split(" - ")
                start_index = months.index(start_month)
                end_index = months.index(end_month)
                highlighted_months = [months[i] for i in range(start_index, end_index + 1)]
            except ValueError:
                highlighted_months = []
        else:
            highlighted_months = []

        return {'months': months, 'highlighted_months': highlighted_months}



class VrtnaBiljkaCreateView(CreateView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_form.html'
    fields = ['ime_v', 'regijaBiljke_v', 'vrijemeSazrijevanja_v']  

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)


class VrtnaBiljkaUpdateView(UpdateView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_form.html'
    fields = ['ime_v', 'regijaBiljke_v', 'vrijemeSazrijevanja_v']
    template_name = 'main/vrtna_biljka_update.html'
    success_url = reverse_lazy('PZWapp:vrtnabiljka_list')

class VrtnaBiljkaDeleteView(DeleteView):
    model = VrtnaBiljka
    template_name = 'main/vrtna_biljka_confirm_delete.html'
    success_url = reverse_lazy('PZWapp:vrtnabiljka_list')

class PovrtnaBiljkaListView(ListView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_list.html'
    context_object_name = 'biljke'

    def get_queryset(self):
        query = self.request.GET.get('q')
        biljke = PovrtnaBiljka.objects.filter(user=self.request.user)  
        if query:
            biljke = biljke.filter(ime_p__icontains=query)
        return biljke

class PovrtnaBiljkaCreateView(CreateView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_form.html'
    form_class = PovrtnaBiljkaForm  
    success_url = reverse_lazy('PZWapp:povrtnabiljka_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)


class PovrtnaBiljkaUpdateView(UpdateView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_form.html'
    fields = ['ime_p', 'regijaBiljke_p', 'vrijemeSazrijevanja_p']
    template_name = 'main/povrtna_biljka_update.html'
    success_url = reverse_lazy('PZWapp:povrtnabiljka_list')

class PovrtnaBiljkaDeleteView(DeleteView):
    model = PovrtnaBiljka
    template_name = 'main/povrtna_biljka_confirm_delete.html'
    success_url = reverse_lazy('PZWapp:povrtnabiljka_list')

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

        if vrijeme_sazrijevanja:
            try:
                start_month, end_month = vrijeme_sazrijevanja.split(" - ")
                start_index = months.index(start_month)
                end_index = months.index(end_month)
                highlighted_months = [months[i] for i in range(start_index, end_index + 1)]
            except ValueError:
                highlighted_months = []
        else:
            highlighted_months = []

        return {'months': months, 'highlighted_months': highlighted_months}

def lista_farmi(request):
    farme = Farma.objects.all()
    return render(request, 'farme/lista.html', {'farme': farme})

def dodaj_farmu(request):
    if request.method == "POST":
        form = FarmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_farmi')
    else:
        form = FarmaForm()
    return render(request, 'farme/dodaj.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import VrtnaBiljka, Farma, FarmaBiljka

@login_required
def dodaj_biljku_na_farmu(request):
    user = request.user
    farme = user.farme.all() 

    if request.method == "POST":
        biljka_id = request.POST.get("biljka")
        farma_id = request.POST.get("farma")
        kolicina = request.POST.get("kolicina")

      
        if not (biljka_id and farma_id and kolicina):
            return render(request, "vrtna_biljka_form.html", {
                "vrtne_biljke": VrtnaBiljka.objects.all(),
                "farme": farme,
                "error": "Molimo popunite sva polja."
            })

        try:
            biljka = VrtnaBiljka.objects.get(id=biljka_id)
            farma = get_object_or_404(Farma, id=farma_id, user=user) 

            FarmaBiljka.objects.create(
                farma=farma,
                biljka_vrtna=biljka,
                kolicina=int(kolicina)
            )
            return redirect("PZWapp:vrtnabiljka_list")

        except VrtnaBiljka.DoesNotExist:
            return render(request, "vrtna_biljka_form.html", {
                "vrtne_biljke": VrtnaBiljka.objects.all(),
                "farme": farme,
                "error": "Odabrana biljka ne postoji."
            })

    return render(request, "vrtna_biljka_form.html", {
        "vrtne_biljke": VrtnaBiljka.objects.all(),
        "farme": farme
    })


