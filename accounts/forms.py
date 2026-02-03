from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Nome de Usuário', widget=forms.TextInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'Seu nome de usuário'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'email@exemplo.com'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'Digite sua senha'}))
    confirm_password = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'Digite a senha novamente'}))

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("As senhas não conferem.")

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'Usuário ou Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'Senha'}))