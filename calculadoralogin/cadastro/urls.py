from django.urls import path
from . import views

app_name = 'cadastro'

urlpatterns = [
    path('', views.Login, name = 'login'),
    path('logar', views.Logar, name = 'logar'),
    path('cadastro', views.PaginaFormCadastro, name = 'cadastro'),
    path('cadastrar', views.Cadastrar, name = 'cadastrar')
]