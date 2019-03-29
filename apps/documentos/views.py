from django.shortcuts import render
from django.views.generic import CreateView
from apps.documentos.models import Documentos

class CreateDocumento(CreateView):
    model = Documentos
    fields = ['descricao', 'arquivo']

    def form_valid(self, form):
        documento = form.save(commit=False)
        documento.funcionario = self.request.user.funcionario
        documento.save()
        return super(CreateDocumento, self).form_valid(form)

