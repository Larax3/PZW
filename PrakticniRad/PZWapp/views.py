from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect


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