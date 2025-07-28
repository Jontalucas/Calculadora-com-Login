from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('idusuario','email', 'nome', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    ordering = ('email',)
    search_fields = ('email', 'nome', 'idusuario')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('nome',)}),
        ('Permissões', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'is_staff', 'is_superuser')}
        ),
    )

admin.site.register(Usuario, UsuarioAdmin)