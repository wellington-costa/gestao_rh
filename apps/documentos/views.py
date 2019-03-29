from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.documentos.models import Documentos

class CreateDocumento(CreateView):
    model = Documentos
    fields = ['descricao', 'arquivo']


    def get_success_url(self):

        return reverse_lazy('update_funcionario')



    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.funcionario_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)




