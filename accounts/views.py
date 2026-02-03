from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm # Vamos criar jajá
from orders.models import Order

@login_required
def dashboard(request):
    # Pega os pedidos do usuário logado
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'accounts/dashboard.html', {'orders': orders})

def account_register(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('accounts:dashboard')
    else:
        registerForm = RegistrationForm()
        
    return render(request, 'accounts/register.html', {'form': registerForm})