from django.shortcuts import render
from .forms import CalculadoraForm
from .models import Operacao

def calculadora_view(request):
    resultado = None

    if request.method == 'POST':
        form = CalculadoraForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data['numero1']
            n2 = form.cleaned_data['numero2']
            op = form.cleaned_data['operacao']

            try:
                if op == '+':
                    resultado = n1 + n2
                elif op == '-':
                    resultado = n1 - n2
                elif op == '*':
                    resultado = n1 * n2
                elif op == '/':
                    resultado = n1 / n2

                Operacao.objects.create(numero1=n1, numero2=n2, operacao=op, resultado=resultado)

            except ZeroDivisionError:
                resultado = 'Erro: divisão por zero'

    else:
        form = CalculadoraForm()

    historico = Operacao.objects.order_by('-criado_em')[:10]  # últimos 10

    return render(request, 'calculadora.html', {
        'form': form,
        'resultado': resultado,
        'historico': historico
    })
