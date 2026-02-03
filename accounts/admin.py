from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Campos que aparecem na lista de usuários (colunas)
    list_display = ('email', 'first_name', 'last_name', 'cpf', 'phone', 'is_staff')
    
    # Adiciona CPF e Telefone na tela de EDIÇÃO do usuário
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Pessoais Extras', {'fields': ('cpf', 'phone')}),
    )
    
    # Configura que o login no admin será por email (opcional, mas bom)
    ordering = ('email',)