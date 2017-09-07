from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from vendas.models import TipoContato, Venda, Reposicao
from vendas.forms import VendaForm, VendaProdutoFormSet, \
   ReposicaoForm, ReposicaoProdutoFormSet, \
   TipoContatoForm


# Create your views here.

### Ambiente de Vendas

class VendasHomeView(TemplateView):
   template_name = 'vendas_home.html'


### venda
class VendaListView(ListView):
   model = Venda
   form_class = VendaForm
   template_name = 'venda_list.html'


class VendaDetailView(DetailView):
   model = Venda
   form_class = VendaForm
   template_name = 'venda_detail.html'


class VendaCreateView(CreateView):
   model = Venda
   form_class = VendaForm
   template_name = 'venda_create.html'
   success_url = 'venda_list'

   def get(self, request, *args, **kwargs):
      """
      Handles GET requests and instantiates blank versions of the form
      and its inline formsets.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      venda_produto_form = VendaProdutoFormSet()
      return self.render_to_response(
         self.get_context_data(
            form=form,
            venda_produto_form=venda_produto_form,
         )
      )

   def post(self, request, *args, **kwargs):
      """
      Handles POST requests, instantiating a form instance and its inline
      formsets with the passed POST variables and then checking them for
      validity.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      venda_produto_form = VendaProdutoFormSet(self.request.POST)
      if (form.is_valid() and venda_produto_form.is_valid()):
         return self.form_valid(form, venda_produto_form)
      else:
         return self.form_invalid(form, venda_produto_form)

   def form_valid(self, form, venda_produto_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      self.object = form.save()
      venda_produto_form.instance = self.object
      venda_produto_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, venda_produto_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      return self.render_to_response(
         self.get_context_data(
            form=form,
            venda_produto_form=venda_produto_form,
         )
      )


class VendaUpdateView(UpdateView):
   model = Venda
   form_class = VendaForm
   template_name = 'venda_update.html'
   success_url = 'venda_list'
   success_url = 'venda_list'

   def get(self, request, *args, **kwargs):
      """
      Handles GET requests and instantiates blank versions of the form
      and its inline formsets.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      venda_produto_form = VendaProdutoFormSet()
      return self.render_to_response(
         self.get_context_data(
            form=form,
            venda_produto_form=venda_produto_form,
         )
      )

   def post(self, request, *args, **kwargs):
      """
      Handles POST requests, instantiating a form instance and its inline
      formsets with the passed POST variables and then checking them for
      validity.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      venda_produto_form = VendaProdutoFormSet(self.request.POST)
      if (form.is_valid() and venda_produto_form.is_valid()):
         return self.form_valid(form, venda_produto_form)
      else:
         return self.form_invalid(form, venda_produto_form)

   def form_valid(self, form, venda_produto_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      self.object = form.save()
      venda_produto_form.instance = self.object
      venda_produto_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, venda_produto_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      return self.render_to_response(
         self.get_context_data(
            form=form,
            venda_produto_form=venda_produto_form,
         )
      )


class VendaDeleteView(DeleteView):
   model = Venda
   form_class = VendaForm
   template_name = 'venda_delete_confirm.html'
   success_url = 'venda_list'


### Tipo_Contato
class TipoContatoListView(ListView):
   model = TipoContato
   template_name = 'tipo_contato_list.html'


class TipoContatoDetailView(DetailView):
   model = TipoContato
   form_class = TipoContatoForm
   template_name = 'tipo_contato_detail.html'


class TipoContatoCreateView(CreateView):
   model = TipoContato
   form_class = TipoContatoForm
   template_name = 'tipo_contato_create.html'
   success_url = 'tipo_contato_list'


class TipoContatoUpdateView(UpdateView):
   model = TipoContato
   form_class = TipoContatoForm
   template_name = 'tipo_contato_create.html'
   success_url = 'tipo_contato_list'


class TipoContatoDeleteView(DeleteView):
   model = TipoContato
   form_class = TipoContatoForm
   template_name = 'tipo_contato_delete_confirm.html'
   success_url = 'tipo_contato_list'


### reposicao
class ReposicaoListView(ListView):
   model = Reposicao
   form_class = ReposicaoForm
   template_name = 'reposicao_list.html'


class ReposicaoDetailView(DetailView):
   model = Reposicao
   form_class = ReposicaoForm
   template_name = 'reposicao_detail.html'


class ReposicaoCreateView(CreateView):
   model = Reposicao
   form_class = ReposicaoForm
   template_name = 'reposicao_create.html'
   success_url = 'reposicao_list'

   def get(self, request, *args, **kwargs):
      """
      Handles GET requests and instantiates blank versions of the form
      and its inline formsets.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      reposicao_produto_form = ReposicaoProdutoFormSet()
      return self.render_to_response(
         self.get_context_data(
            form=form,
            reposicao_produto_form=reposicao_produto_form,
         )
      )

   def post(self, request, *args, **kwargs):
      """
      Handles POST requests, instantiating a form instance and its inline
      formsets with the passed POST variables and then checking them for
      validity.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      reposicao_produto_form = ReposicaoProdutoFormSet(self.request.POST)
      if (form.is_valid() and reposicao_produto_form.is_valid()):
         return self.form_valid(form, reposicao_produto_form)
      else:
         return self.form_invalid(form, reposicao_produto_form)

   def form_valid(self, form, reposicao_produto_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      self.object = form.save()
      reposicao_produto_form.instance = self.object
      reposicao_produto_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, reposicao_produto_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      return self.render_to_response(
         self.get_context_data(
            form=form,
            reposicao_produto_form=reposicao_produto_form,
         )
      )


class ReposicaoUpdateView(UpdateView):
   model = Reposicao
   form_class = ReposicaoForm
   template_name = 'reposicao_update.html'
   success_url = 'reposicao_list'


class ReposicaoDeleteView(DeleteView):
   model = Reposicao
   form_class = ReposicaoForm
   template_name = 'reposicao_delete_confirm.html'
   success_url = 'reposicao_list'
