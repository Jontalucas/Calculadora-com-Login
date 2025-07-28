from django.shortcuts import redirect, render
from .models import Usuario
from django.contrib.auth import authenticate, login
from .forms import FormularioCadastro, FormularioLogin
from django.http import  Http404
from django.contrib import messages
from django.urls import reverse

# View da página do formulário de cadastro
def PaginaFormCadastro(request):
    formulario_cadastro = request.session.get('formulario_cadastro', None)
    form = FormularioCadastro(formulario_cadastro)
    return render(request, 'cadastro.html', {'form': form})

#Função para cadastrar
def Cadastrar(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['formulario_cadastro'] = POST
    form = FormularioCadastro(POST)
    if form.is_valid():
        form.save()
        del(request.session['formulario_cadastro'])
        return redirect('cadastro:Login')
    
    return redirect('cadastro:Cadastro')

def Login(request):
    form = FormularioLogin()
    return render(request, 'login.html', {'form' : form, 'form_action': reverse('cadastro:Logar')})

def Logar(request):
    if not request.POST:
        raise Http404()

    form = FormularioLogin(request.POST)

    if form.is_valid():
        autenticado = authenticate(
            email=form.cleaned_data.get('Email', ''),
            senha=form.cleaned_data.get('Senha', ''),
        )

        if autenticado:
            login(request, autenticado)
            return redirect(reverse('calculadora:Calculadora'))
        else:
            messages.error(request, 'Invalid username or password')
    else:
        messages.error(request, 'Invalid username or password')
    return redirect('cadastro:Login')
    
    
        

