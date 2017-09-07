from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from relacionamento.models import Cliente
from relacionamento.forms import ClienteDetailForm, ClienteCreateUpdateForm, \
   ClienteDeleteForm, ClienteActiveForm, ClienteBlockForm


# Create your views here.

class RelacionamentoHomeView(TemplateView):
   template_name = 'relacionamento_home.html'


class ClienteListView(ListView):
   model = Cliente
   template_name = 'cliente_list.html'
   fields = [
      'nome_preferencial',
      'endereco',
      'watsapp',
      'interfone',
   ]

   def get_queryset(self):
      qs = super(ClienteListView, self).get_queryset()
      qs = qs.filter(esta_excluido__exact=False, esta_bloqueado__exact=False)
      return qs


class ClienteCreateView(CreateView):
   model = Cliente
   form_class = ClienteCreateUpdateForm
   template_name = 'cliente_create.html'
   success_url = reverse_lazy('cliente_list')


class ClienteDetailView(DetailView):
   model = Cliente
   form_class = ClienteDetailForm
   template_name = 'cliente_detail.html'


class ClienteUpdateView(UpdateView):
   model = Cliente
   form_class = ClienteCreateUpdateForm
   template_name = 'cliente_update.html'
   success_url = reverse_lazy('cliente_list')


class ClienteDeleteView(DeleteView):
   model = Cliente
   form_class = ClienteDeleteForm
   template_name = 'cliente_delete_confirm.html'
   success_url = reverse_lazy('cliente_list')


class ClienteActiveView(UpdateView):
   model = Cliente
   form_class = ClienteActiveForm
   template_name = 'cliente_active.html'
   success_url = reverse_lazy('cliente_list')


class ClienteBlockView(UpdateView):
   model = Cliente
   form_class = ClienteBlockForm
   template_name = 'cliente_block.html'
   success_url = reverse_lazy('cliente_list')
