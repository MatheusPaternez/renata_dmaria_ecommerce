from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'Nome'}))
    last_name = forms.CharField(label='Sobrenome', widget=forms.TextInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'Sobrenome'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'email@exemplo.com'}))
    cpf = forms.CharField(label='CPF', widget=forms.TextInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': '000.000.000-00'}))
    phone = forms.CharField(label='Telefone', widget=forms.TextInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': '(12) 99999-9999'}))
    
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'Senha'}))
    confirm_password = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'Repita a senha'}))
    
    username = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'cpf', 'phone')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("As senhas não conferem.")
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        # Se o username vier vazio, usa o email como username
        if not user.username:
            user.username = user.email
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', widget=forms.TextInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'Email'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(
        attrs={'class': 'w-full border p-2 rounded mb-4', 'placeholder': 'Senha'}))