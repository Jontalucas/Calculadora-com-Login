from django.db import models
from Cadastro.models import Usuario

# Create your models here.
class Operacao(models.Model):
    IDOperacao = models.AutoField(primary_key=True)
    IDUsuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    Parametros = models.CharField(null=False, blank=False)
    Resultado = models.CharField(null=False, blank=False)
    DtInclusao = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'Operacao'