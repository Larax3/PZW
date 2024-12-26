from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import VrtnaBiljka, PovrtnaBiljka
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Views for authentication and authorization
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('PZWapp:homepage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def homepage(request):
    return render(request, 'main/homepage.html')

@login_required
def admin_view(request):
    if not request.user.is_superuser:
        return HttpResponse('Unauthorized', status=401)
    users = User.objects.all()
    return render(request, 'main/admin_view.html', {'users': users})

@login_required
def delete_user(request, user_id):
    if not request.user.is_superuser:
        return HttpResponse('Unauthorized', status=401)
    try:
        user = User.objects.get(pk=user_id)
        user.delete()
        return redirect('PZWapp:admin_view')
    except User.DoesNotExist:
        return HttpResponse('User not found', status=404)

def custom_logout(request):
    logout(request)
    return redirect('login')

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

from django.http import HttpResponse
from .models import VrtnaBiljka, PovrtnaBiljka

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