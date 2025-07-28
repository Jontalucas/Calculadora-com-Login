from django.db import models
from cadastro.models import Usuario

from django.db import models

class Operacao(models.Model):
    numero1 = models.FloatField()
    numero2 = models.FloatField()
    operacao = models.CharField(max_length=1)  # '+', '-', '*', '/'
    resultado = models.FloatField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numero1} {self.operacao} {self.numero2} = {self.resultado}"
