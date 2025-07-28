from django import forms
from .views import Usuario

class FormularioCadastro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class FormularioLogin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'Email',
            'Senha'
        ]