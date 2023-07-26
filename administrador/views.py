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

def recuperar(request):
    return render(request, 'recuperar.html')

def signout(request):
    logout(request)
    return redirect('home')

@login_required
def administrador(request):
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


#restablecer
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# Vista personalizada para enviar correos de restablecimiento de contraseña
class MyPasswordResetView(PasswordResetView):
    template_name = 'reestablecer/reset_recuperar.html'
    success_url = reverse_lazy('password_reset_done')
    email_template_name = 'reestablecer/password_reset_email.html'
    subject_template_name = 'reestablecer/password_reset_subject.txt'

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'reestablecer/reset_enviado.html'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reestablecer/reset_nueva.html'
    success_url = reverse_lazy('password_reset_complete')

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'reestablecer/reset_confirmacion.html'


from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserRegistrationForm, LoginForm, BloqueForm
from django.contrib.auth import authenticate, login as auth_login, logout
from sitios.models import Bloque, Sitio
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Resto de tus vistas ...

# Nueva vista para enviar correos de restablecimiento de contraseña
class MyPasswordResetView(PasswordResetView):
    template_name = 'reestablecer/reset_recuperar.html'
    success_url = reverse_lazy('password_reset_done')
    email_template_name = 'reestablecer/password_reset_email.html'
    subject_template_name = 'reestablecer/password_reset_subject.txt'


from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib import messages

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reestablecer/reset_nueva.html'
    success_url = reverse_lazy('password_reset_complete')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            messages.success(request, '¡Contraseña restablecida con éxito! Ahora puedes iniciar sesión con tu nueva contraseña.')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


