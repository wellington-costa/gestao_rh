from django.db import models
from apps.funcionarios.models import Funcionario

class Documentos(models.Model):
    descricao = models.CharField(max_length=20)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao

