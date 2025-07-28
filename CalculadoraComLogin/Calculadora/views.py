from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# View da página da calculadora
def Calculadora(request):
    return render(request, 'calculadora.html')

@login_required(login_url='cadastro:Login', redirect_field_name='next')
def Logout(request):
    if not request.POST:
        return redirect(reverse('cadastro:Login'))

    if request.POST.get('email') != request.user.email:
        return redirect(reverse('cadastro:Login'))

    logout(request)
    return redirect(reverse('cadastro:Login'))