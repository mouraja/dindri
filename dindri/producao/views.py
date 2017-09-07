from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from producao.models import TipoBase, \
   TipoProduto, \
   TipoSabor, Insumo, \
   Base, \
   Sabor, \
   Produto, \
   LoteBase, LoteSabor, LoteProduto
from producao.forms import \
   TipoBaseCreateUpdateForm, TipoBaseActiveForm, TipoBaseDetailForm, TipoBaseDeleteForm, \
   TipoSaborCreateUpdateForm, TipoSaborActiveForm, TipoSaborDetailForm, TipoSaborDeleteForm, \
   TipoProdutoCreateUpdateForm, TipoProdutoActiveForm, TipoProdutoDetailForm, TipoProdutoDeleteForm, \
   ProdutoForm, ProdutoCreateForm, ProdutoSaborFormSet, ProdutoInsumoFormSet, \
   BaseForm, BaseInsumoFormSet, \
   SaborForm, SaborInsumoFormSet, SaborBaseFormSet, \
   LoteBaseForm, LoteSaborForm, LoteProdutoForm, InsumoForm


# Create your views here.

### Ambiente de producao

### Home
class ProducaoHomeView(TemplateView):
   template_name = 'producao_home.html'


### Base
class BaseListView(ListView):
   model = Base
   form_class = BaseForm
   template_name = 'base_list.html'


class BaseDetailView(ListView):
   model = Base
   form_class = BaseForm
   template_name = 'base_detail.html'


class BaseCreateView(CreateView):
   model = Base
   form_class = BaseForm
   template_name = 'base_create.html'
   success_url = 'base_list'

   def get(self, request, *args, **kwargs):
      """
      Handles GET requests and instantiates blank versions of the form
      and its inline formsets.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      base_insumo_form = BaseInsumoFormSet()
      return self.render_to_response(
         self.get_context_data(
            form=form,
            base_insumo_form=base_insumo_form,
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
      base_insumo_form = BaseInsumoFormSet(self.request.POST)
      if (form.is_valid() and base_insumo_form.is_valid()):
         return self.form_valid(form, base_insumo_form)
      else:
         return self.form_invalid(form, base_insumo_form)

   def form_valid(self, form, base_insumo_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      self.object = form.save()
      base_insumo_form.instance = self.object
      base_insumo_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, base_insumo_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      return self.render_to_response(
         self.get_context_data(
            form=form,
            base_insumo_form=base_insumo_form,
         )
      )


class BaseUpdateView(UpdateView):
   model = Base
   form_class = BaseForm
   template_name = 'base_update.html'


class BaseDeleteView(DeleteView):
   model = Base
   form_class = BaseForm
   template_name = 'base_delete.html'


### Sabor
class SaborListView(ListView):
   model = Sabor
   form_class = SaborForm
   template_name = 'sabor_list.html'


class SaborDetailView(DetailView):
   model = Sabor
   form_class = SaborForm
   template_name = 'sabor_detail.html'


class SaborCreateView(CreateView):
   model = Sabor
   form_class = SaborForm
   template_name = 'sabor_create.html'
   success_url = 'sabor_list'

   def get(self, request, *args, **kwargs):
      """
      Handles GET requests and instantiates blank versions of the form
      and its inline formsets.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      sabor_base_form = SaborBaseFormSet()
      sabor_insumo_form = SaborInsumoFormSet()
      return self.render_to_response(
         self.get_context_data(
            form=form,
            sabor_base_form=sabor_base_form,
            sabor_insumo_form=sabor_insumo_form,
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
      sabor_base_form = SaborBaseFormSet(self.request.POST)
      sabor_insumo_form = SaborInsumoFormSet(self.request.POST)
      if (form.is_valid() and sabor_base_form.is_valid() and
             sabor_insumo_form.is_valid()):
         return self.form_valid(form, sabor_base_form, sabor_insumo_form)
      else:
         return self.form_invalid(form, sabor_base_form, sabor_insumo_form)

   def form_valid(self, form, sabor_base_form, sabor_insumo_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      self.object = form.save()
      sabor_base_form.instance = self.object
      sabor_base_form.save()
      sabor_insumo_form.instance = self.object
      sabor_insumo_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, sabor_base_form, sabor_insumo_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      return self.render_to_response(
         self.get_context_data(
            form=form,
            sabor_base_form=sabor_base_form,
            sabor_insumo_form=sabor_insumo_form,
         )
      )


class SaborUpdateView(DetailView):
   model = Sabor
   form_class = SaborForm
   template_name = 'sabor_update.html'


class SaborDeleteView(DeleteView):
   model = Sabor
   form_class = SaborForm
   template_name = 'sabor_delete.html'


### Produto
class ProdutoListView(ListView):
   model = Produto
   form_class = ProdutoForm
   template_name = 'produto_list.html'


class ProdutoDetailView(DetailView):
   model = Produto
   form_class = ProdutoForm
   template_name = 'produto_detail.html'


class ProdutoCreateView(CreateView):
   model = Produto
   form_class = ProdutoCreateForm
   template_name = 'produto_create.html'
   success_url = 'produto_list'

   def get(self, request, *args, **kwargs):
      """
      Handles GET requests and instantiates blank versions of the form
      and its inline formsets.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      produto_sabor_form = ProdutoSaborFormSet()
      produto_insumo_form = ProdutoInsumoFormSet()
      return self.render_to_response(
         self.get_context_data(
            form=form,
            produto_sabor_form=produto_sabor_form,
            produto_insumo_form=produto_insumo_form,
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
      produto_sabor_form = ProdutoSaborFormSet(self.request.POST)
      produto_insumo_form = ProdutoInsumoFormSet(self.request.POST)
      if (form.is_valid() and produto_sabor_form.is_valid() and
             produto_insumo_form.is_valid()):
         return self.form_valid(form, produto_sabor_form, produto_insumo_form)
      else:
         return self.form_invalid(form, produto_sabor_form, produto_insumo_form)

   def form_valid(self, form, produto_sabor_form, produto_insumo_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      self.object = form.save()
      produto_sabor_form.instance = self.object
      produto_sabor_form.save()
      produto_insumo_form.instance = self.object
      produto_insumo_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, produto_sabor_form, produto_insumo_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      return self.render_to_response(
         self.get_context_data(
            form=form,
            produto_sabor_form=produto_sabor_form,
            produto_insumo_form=produto_insumo_form,
         )
      )


class ProdutoUpdateView(UpdateView):
   model = Produto
   form_class = ProdutoForm
   template_name = 'produto_update.html'


class ProdutoDeleteView(DeleteView):
   model = Produto
   form_class = ProdutoForm
   template_name = 'produto_delete.html'


### Tipo_Base
class TipoBaseListView(ListView):
   model = TipoBase
   template_name = 'tipo_base_list.html'
   fields = [
      'nome',
      'descricao',
   ]


class TipoBaseCreateView(CreateView):
   model = TipoBase
   form_class = TipoBaseCreateUpdateForm
   template_name = 'tipo_base_create.html'
   success_url = reverse_lazy('tipo_base_list')


class TipoBaseActiveView(UpdateView):
   model = TipoBase
   form_class = TipoBaseActiveForm
   template_name = 'tipo_base_active.html'
   success_url = reverse_lazy('tipo_base_list')


class TipoBaseDetailView(DetailView):
   model = TipoBase
   form_class = TipoBaseDetailForm
   template_name = 'tipo_base_detail.html'
   success_url = reverse_lazy('tipo_base_list')


class TipoBaseUpdateView(UpdateView):
   model = TipoBase
   form_class = TipoBaseCreateUpdateForm
   template_name = 'tipo_base_update.html'
   success_url = reverse_lazy('tipo_base_list')


class TipoBaseDeleteView(DeleteView):
   model = TipoBase
   form_class = TipoBaseDeleteForm
   template_name = 'tipo_base_delete_confirm.html'
   success_url = reverse_lazy('tipo_base_list')


### Tipo_Produto
class TipoProdutoListView(ListView):
   model = TipoProduto
   template_name = 'tipo_produto_list.html'
   fields = [
      'nome',
      'descricao',
   ]

   def get_queryset(self):
      qs = super(TipoProdutoListView, self).get_queryset()
      qs = qs.filter(esta_excluido__exact=False)
      return qs


class TipoProdutoDetailView(DetailView):
   model = TipoProduto
   form_class = TipoProdutoDetailForm
   template_name = 'tipo_produto_detail.html'


class TipoProdutoCreateView(CreateView):
   model = TipoProduto
   form_class = TipoProdutoCreateUpdateForm
   template_name = 'tipo_produto_create.html'
   success_url = reverse_lazy('tipo_produto_list')


class TipoProdutoUpdateView(UpdateView):
   model = TipoProduto
   form_class = TipoProdutoCreateUpdateForm
   template_name = 'tipo_produto_update.html'
   success_url = reverse_lazy('tipo_produto_list')


class TipoProdutoActiveView(UpdateView):
   model = TipoProduto
   form_class = TipoProdutoActiveForm
   template_name = 'tipo_produto_active.html'
   success_url = reverse_lazy('tipo_produto_list')


class TipoProdutoDeleteView(DeleteView):
   model = TipoProduto
   form_class = TipoProdutoDeleteForm
   template_name = 'tipo_produto_delete_confirm.html'
   success_url = reverse_lazy('tipo_produto_list')


### Tipo_Sabor
class TipoSaborListView(ListView):
   model = TipoSabor
   template_name = 'tipo_sabor_list.html'
   fields = [
      'nome',
      'descricao',
   ]


class TipoSaborCreateView(CreateView):
   model = TipoSabor
   form_class = TipoSaborCreateUpdateForm
   template_name = 'tipo_sabor_create.html'
   success_url = reverse_lazy('tipo_sabor_list')


class TipoSaborActiveView(UpdateView):
   model = TipoSabor
   form_class = TipoSaborActiveForm
   template_name = 'tipo_sabor_active.html'
   success_url = reverse_lazy('tipo_sabor_list')


class TipoSaborDetailView(DetailView):
   model = TipoSabor
   form_class = TipoSaborDetailForm
   template_name = 'tipo_sabor_detail.html'
   success_url = reverse_lazy('tipo_sabor_list')


class TipoSaborUpdateView(UpdateView):
   model = TipoSabor
   form_class = TipoSaborCreateUpdateForm
   template_name = 'tipo_sabor_update.html'
   success_url = reverse_lazy('tipo_sabor_list')


class TipoSaborDeleteView(DeleteView):
   model = TipoSabor
   form_class = TipoSaborDeleteForm
   template_name = 'tipo_sabor_delete_confirm.html'
   success_url = reverse_lazy('tipo_sabor_list')


### Lote Base
class LoteBaseListView(ListView):
   model = LoteBase
   form_class = LoteBaseForm
   template_name = 'lote_base_list.html'


class LoteBaseDetailView(DetailView):
   model = LoteBase
   form_class = LoteBaseForm
   template_name = 'lote_base_detail.html'


class LoteBaseCreateView(CreateView):
   model = LoteBase
   form_class = LoteBaseForm
   template_name = 'lote_base_create.html'


class LoteBaseUpdateView(UpdateView):
   model = LoteBase
   form_class = LoteBaseForm
   template_name = 'lote_base_update.html'


class LoteBaseDeleteView(DeleteView):
   model = LoteBase
   form_class = LoteBaseForm
   template_name = 'lote_base_delete_confirm.html'


### Lote Produto
class LoteProdutoListView(ListView):
   model = LoteProduto
   form_class = LoteProdutoForm
   template_name = 'lote_produto_list.html'


class LoteProdutoDetailView(DetailView):
   model = LoteProduto
   form_class = LoteProdutoForm
   template_name = 'lote_produto_detail.html'


class LoteProdutoCreateView(CreateView):
   model = LoteProduto
   form_class = LoteProdutoForm
   template_name = 'lote_produto_create.html'


class LoteProdutoUpdateView(UpdateView):
   model = LoteProduto
   form_class = LoteProdutoForm
   template_name = 'lote_produto_update.html'


class LoteProdutoDeleteView(DeleteView):
   model = LoteProduto
   form_class = LoteProdutoForm
   template_name = 'lote_produto_delete_confirm.html'


### Lote Insumo
class LoteSaborListView(ListView):
   model = LoteSabor
   form_class = LoteSaborForm
   template_name = 'lote_sabor_list.html'


class LoteSaborDetailView(DetailView):
   model = LoteSabor
   form_class = LoteSaborForm
   template_name = 'lote_sabor_detail.html'


class LoteSaborCreateView(CreateView):
   model = LoteSabor
   form_class = LoteSaborForm
   template_name = 'lote_sabor_create.html'


class LoteSaborUpdateView(UpdateView):
   model = LoteSabor
   form_class = LoteSaborForm
   template_name = 'lote_sabor_update.html'


class LoteSaborDeleteView(DeleteView):
   model = LoteSabor
   form_class = LoteSaborForm
   template_name = 'lote_sabor_delete_confirm.html'


### Insumo
class InsumoListView(ListView):
   model = Insumo
   template_name = 'insumo_list.html'


class InsumoDetailView(DetailView):
   model = Insumo
   form_class = InsumoForm
   template_name = 'insumo_detail.html'


class InsumoCreateView(CreateView):
   model = Insumo
   form_class = InsumoForm
   template_name = 'insumo_create.html'


class InsumoUpdateView(UpdateView):
   model = Insumo
   form_class = InsumoForm
   template_name = 'insumo_update.html'


class InsumoDeleteView(DeleteView):
   model = Insumo
   form_class = InsumoForm
   template_name = 'insumo_delete_confirm.html'
