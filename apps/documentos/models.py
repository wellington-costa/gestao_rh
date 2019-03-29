from django.db import models
from django.db.models import FileField

from apps.funcionarios.models import Funcionario

class Documentos(models.Model):
    descricao = models.CharField(max_length=20)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = FileField(upload_to = 'documentos')

    def __str__(self):
        return self.descricao

