from django.shortcuts import render, redirect
from .forms import FormularioCadastro, FormularioLogin
from django.http import  Http404
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib import messages


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
        return redirect('cadastro:login')
    
    return redirect('cadastro:cadastro')

def Login(request):
    form = FormularioLogin()
    return render(request, 'login.html', {'form' : form, 'form_action': reverse('cadastro:logar')})

def Logar(request):
    if not request.POST:
        raise Http404()

    form = FormularioLogin(request.POST)

    if form.is_valid():
        user = authenticate(
            request,
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )

        if user is not None:
            login(request, user)
            
        else:
            messages.error(request, 'Invalid username or password')
    else:
        messages.error(request, 'Invalid username or password')
    return redirect(reverse('calculadora:calculadora'))