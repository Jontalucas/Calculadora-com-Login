from django.urls import path
from . import views

app_name = 'cadastro'

urlpatterns = [
    path('', views.Login, name = 'Login'),
    path('logar', views.Logar, name = 'Logar'),
    path('cadastro', views.PaginaFormCadastro, name = 'Cadastro'),
    path('cadastrar', views.Cadastrar, name = 'Cadastrar')
]
