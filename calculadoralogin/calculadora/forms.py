from django import forms

OPERACOES = [
    ('+', '+'),
    ('-', '-'),
    ('*', '*'),
    ('/', '/'),
]

class CalculadoraForm(forms.Form):
    numero1 = forms.FloatField(label='Número 1')
    operacao = forms.ChoiceField(choices=OPERACOES, label='Operação')
    numero2 = forms.FloatField(label='Número 2')
