from django import forms
from .models import Usuario

class FormularioCadastro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome',
            'email',
            'password'
        ]

class FormularioLogin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'email',
            'password'
        ]