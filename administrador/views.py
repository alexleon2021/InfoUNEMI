from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserRegistrationForm, LoginForm, BloqueForm
from django.contrib.auth import authenticate, login as auth_login, logout
from sitios.models import Bloque, Sitio
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('administrador')  # Redirecciona a la página de inicio después del inicio de sesión exitoso
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecciona a la página de inicio de sesión después del registro exitoso
    else:
        form = UserRegistrationForm()

    return render(request, 'registrarse.html', {'form': form})

def recuperarC(request):
    return render(request, 'recuperar.html')

def signout(request):
    logout(request)
    return redirect('home')

@login_required
def adminsitrador(request):
    bloques = Bloque.objects.all()
    return render(request, 'administrador.html', {'bloques': bloques})

@login_required
def editar_bloque(request, bloque_id):
    bloque = get_object_or_404(Bloque, id=bloque_id)
    if request.method == 'POST':
        form = BloqueForm(request.POST, instance=bloque)
        if form.is_valid():
            form.save()
            return redirect('administrador')
    else:
        form = BloqueForm(instance=bloque)
    return render(request, 'editar_bloque.html', {'form': form})


