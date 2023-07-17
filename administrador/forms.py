from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from sitios.models import Bloque, Sitio

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class BloqueForm(forms.ModelForm):
    class Meta:
        model = Bloque
        fields = '__all__'
