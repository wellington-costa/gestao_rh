from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Funcionario
from django.views.generic.list import ListView

class CreateFuncionario(CreateView):
     model = Funcionario
     fields = ['nome', 'usuario', 'departamento', 'empresa']

class ListFuncionarios(ListView):
     model = Funcionario

     def get_queryset(self):
          empresa_logada = self.request.user.funcionario.empresa
          queryset = Funcionario.objects.filter(empresa = empresa_logada)
          return queryset

class UpadteFuncionarios(UpdateView):
     model = Funcionario
     fields = ['nome', 'departamento']

class DeleteFuncionario(DeleteView):
     model = Funcionario
     success_url = reverse_lazy('list_funcionarios')



