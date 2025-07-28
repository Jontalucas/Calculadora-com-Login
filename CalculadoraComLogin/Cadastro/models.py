from django.db import models

# Model da tabela usuario
class Usuario(models.Model):
    IDUsuario = models.AutoField(primary_key=True)
    Nome = models.CharField(null=False, blank=False)
    Email = models.CharField(null=False, blank=False)
    Senha = models.CharField(null=False, blank=False)
    DtInclusao = models.DateField(null=False, auto_now_add=True)
    
    class Meta:
        db_table = 'Usuario'