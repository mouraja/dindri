from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from compras.models import Fornecedor, Compra, CompraItem, Pedido, PedidoItem
from compras.forms import FornecedorCreateUpdateForm, FornecedorActiveForm
from compras.forms import FornecedorDetailForm, FornecedorDeleteForm
from compras.forms import CompraForm, CompraCreateForm, CompraUpdateForm
from compras.forms import CompraDoneForm, CompraCancelForm
from compras.forms import CompraItemCreateFormSet, CompraItemUpdateFormSet
from compras.forms import CompraItemDoneFormSet, CompraItemCancelFormSet
from compras.forms import PedidoForm, PedidoCreateForm, PedidoUpdateForm
from compras.forms import PedidoItemCreateFormSet, PedidoItemUpdateFormSet


# Create your views here.

## Compras
class ComprasHomeView(TemplateView):
   template_name = 'compras_home.html'

## Fornecedor
class FornecedorListView(ListView):
   model = Fornecedor
   template_name = 'fornecedor_list.html'
   fields = [
      'tipo_fornecedor',
      'nome',
      'nome_fantasia',
      'cnpj',
      'logradouro',
      'complemento',
      'bairro',
      'cidade',
      'uf',
      'cep',
      'telefone',
      'contato',
      'email',
      'observacao',
   ]

class FornecedorCreateView(CreateView):
   model = Fornecedor
   form_class = FornecedorCreateUpdateForm
   template_name = 'fornecedor_create.html'
   success_url = reverse_lazy('fornecedor_list')

class FornecedorUpdateView(UpdateView):
   model = Fornecedor
   form_class = FornecedorCreateUpdateForm
   template_name = 'fornecedor_update.html'
   success_url = reverse_lazy('fornecedor_list')

class FornecedorDetailView(DetailView):
   model = Fornecedor
   form_class = FornecedorDetailForm
   template_name = 'fornecedor_detail.html'
   success_url = reverse_lazy('fornecedor_list')

class FornecedorDeleteView(DeleteView):
   model = Fornecedor
   form_class = FornecedorDeleteForm
   template_name = 'fornecedor_delete_confirm.html'
   success_url = reverse_lazy('fornecedor_list')

class FornecedorActiveView(UpdateView):
   model = Fornecedor
   form_class = FornecedorActiveForm
   template_name = 'fornecedor_active.html'
   success_url = reverse_lazy('fornecedor_list')

## Compra
class CompraListView(ListView):
   model = Compra
   form_class = CompraForm
   template_name = 'compra_list.html'
   fields = [
      'pedido'
      'data_compra'
      'valor_total'
   ]

class CompraDetailView(DetailView):
   model = Compra
   form_class = CompraForm
   template_name = 'compra_detail.html'

class CompraCreateView(CreateView):
   model = Compra
   form_class = CompraCreateForm
   template_name = 'compra_create.html'
   success_url = reverse_lazy('compra_list')

   def get(self, request, *args, **kwargs):
      """
      Handles GET requests and instantiates blank versions of the form
      and its inline formsets.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      compraitem_form = CompraItemCreateFormSet()
      return self.render_to_response(
         self.get_context_data(
            form=form,
            compraitem_form=compraitem_form,
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
      compraitem_form = CompraItemCreateFormSet(self.request.POST)
      if (form.is_valid() and compraitem_form.is_valid()):
         return self.form_valid(form, compraitem_form)
      else:
         return self.form_invalid(form, compraitem_form)

   def form_valid(self, form, compraitem_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      self.object = form.save()
      compraitem_form.instance = self.object
      compraitem_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, compraitem_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      return self.render_to_response(
         self.get_context_data(
            form=form,
            compraitem_form=compraitem_form,
         )
      )

class CompraUpdateView(UpdateView):
   model = Compra
   form_class = CompraUpdateForm
   template_name = 'compra_update.html'
   success_url = reverse_lazy('compra_list')

   def get_context_data(self, **kwargs):
      context = super(CompraUpdateView, self).get_context_data(**kwargs)
      if self.request.POST:
         context['form'] = CompraUpdateForm(self.request.POST, instance=self.object)
         context['compraitem_form'] = CompraItemUpdateFormSet(self.request.POST, instance=self.object)
      else:
         context['form'] = CompraUpdateForm(instance=self.object)
         context['compraitem_form'] = CompraItemUpdateFormSet(instance=self.object)
      return context

   def post(self, request, *args, **kwargs):
      """
      Handles POST requests, instantiating a form instance and its inline
      formsets with the passed POST variables and then checking them for
      validity.
      """
      self.object = self.get_object()
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      compraitem_form = CompraItemUpdateFormSet(self.request.POST, instance=self.object)
      if form.is_valid():
         print("Fui form.is_valid")
      if compraitem_form.is_valid():
         print("Fui form.is_valid")
      if (form.is_valid() and compraitem_form.is_valid()):
         return self.form_valid(form, compraitem_form)
      else:
         return self.form_invalid(form, compraitem_form)

   def form_valid(self, form, compraitem_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      self.object = form.save()
      compraitem_form.instance = self.object
      compraitem_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, compraitem_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      return self.render_to_response(
         self.get_context_data(
            form=form,
            compraitem_form=compraitem_form,
         )
      )

class CompraDoneView(UpdateView):
   model = Compra
   form_class = CompraDoneForm
   template_name = 'compra_done.html'
   success_url = reverse_lazy('compra_list')

class CompraDoneView1(UpdateView):
   model = Compra
   form_class = CompraDoneForm
   template_name = 'compra_done2.html'
   success_url = reverse_lazy('compra_list')

   def get_context_data(self, **kwargs):
      print('estou no get_context_data')
      context = super(CompraDoneView, self).get_context_data(**kwargs)
      if self.request.POST:
         context['form'] = CompraDoneForm(self.request.POST, instance=self.object)
         context['compraitem_form'] = CompraItemDoneFormSet(self.request.POST, instance=self.object)
      else:
         context['form'] = CompraDoneForm(instance=self.object)
         context['compraitem_form'] = CompraItemDoneFormSet(instance=self.object)
      return context

   def post(self, request, *args, **kwargs):
      """
      Handles POST requests, instantiating a form instance and its inline
      formsets with the passed POST variables and then checking them for
      validity.
      """
      print('estou no post')
      self.object = self.get_object()
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      compraitem_form = CompraItemDoneFormSet(self.request.POST)
      if not form.is_valid():
         print('form.is_valid error')
      if not compraitem_form.is_valid():
         print('compraitem_form.is_valid error')
      if (form.is_valid() and compraitem_form.is_valid()):
         return self.form_valid(form, compraitem_form)
      else:
         return self.form_invalid(form, compraitem_form)

   def form_valid(self, form, compraitem_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      print('estou form_valid')
      self.object = form.save()
      compraitem_form.instance = self.object
      compraitem_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, compraitem_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      print('estou no form_invalid')
      return self.render_to_response(
         self.get_context_data(
            form=form,
            compraitem_form=compraitem_form,
         )
      )

class CompraCancelView(UpdateView):
   model = Compra
   form_class = CompraCancelForm
   template_name = 'compra_cancel.html'
   success_url = reverse_lazy('compra_list')

   def get_context_data(self, **kwargs):
      context = super(CompraCancelView, self).get_context_data(**kwargs)
      if self.request.POST:
         context['form'] = CompraCancelForm(self.request.POST, instance=self.object)
         context['compraitem_form'] = CompraItemCancelFormSet(self.request.POST, instance=self.object)
      else:
         context['form'] = CompraCancelForm(instance=self.object)
         context['compraitem_form'] = CompraItemCancelFormSet(instance=self.object)
      return context

   def post(self, request, *args, **kwargs):
      """
      Handles POST requests, instantiating a form instance and its inline
      formsets with the passed POST variables and then checking them for
      validity.
      """
      self.object = self.get_object()
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      compraitem_form = CompraItemCancelFormSet(self.request.POST, instance=self.object)
      if (form.is_valid() and compraitem_form.is_valid()):
         return self.form_valid(form, compraitem_form)
      else:
         return self.form_invalid(form, compraitem_form)

   def form_valid(self, form, compraitem_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      self.object = form.save()
      compraitem_form.instance = self.object
      compraitem_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, compraitem_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      return self.render_to_response(
         self.get_context_data(
            form=form,
            compraitem_form=compraitem_form,
         )
      )

class CompraDeleteView(DeleteView):
   model = Compra
   form_class = CompraForm
   template_name = 'compra_delete_confirm.html'
   success_url = reverse_lazy('compra_list')

## Pedido
class PedidoListView(ListView):
   model = Pedido
   form_class = PedidoForm
   template_name = 'pedido_list.html'
   '''paginate_by = 15
   ordering = ['-data_limite']
   success_url = reverse_lazy('pedido_list')
   '''
   def get_queryset(self):
      qs = super(PedidoListView, self).get_queryset()
      qs = qs.filter(esta_excluido__exact=False, esta_bloqueado__exact=False)
      return qs

class PedidoDetailView(DetailView):
   model = Pedido
   form_class = PedidoForm
   template_name = 'pedido_detail.html'
   success_url = reverse_lazy('pedido_list')

class PedidoUpdateView(UpdateView):
   model = Pedido
   form_class = PedidoUpdateForm
   template_name = 'pedido_update.html'
   success_url = reverse_lazy('pedido_list')

   def get(self, request, *args, **kwargs):
      """
      Handles GET requests and instantiates blank versions of the form
      and its inline formsets.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      pedidoitem_form = PedidoItemUpdateFormSet()
      return self.render_to_response(
         self.get_context_data(
            form=form,
            pedidoitem_form=pedidoitem_form,
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
      pedidoitem_form = PedidoItemUpdateFormSet(self.request.POST)
      if (form.is_valid() and pedidoitem_form.is_valid()):
         return self.form_valid(form, pedidoitem_form)
      else:
         return self.form_invalid(form, pedidoitem_form)

   def form_valid(self, form, pedidoitem_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      self.object = form.save()
      pedidoitem_form.instance = self.object
      pedidoitem_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, pedidoitem_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      return self.render_to_response(
         self.get_context_data(
            form=form,
            pedidoitem_form=pedidoitem_form,
         )
      )

class PedidoActiveView(UpdateView):
   model = Pedido
   form_class = PedidoForm
   template_name = 'pedido_active.html'
   success_url = reverse_lazy('pedido_list')

class PedidoDeleteView(DeleteView):
   model = Pedido
   form_class = PedidoForm
   template_name = 'pedido_delete_confirm.html'
   success_url = reverse_lazy('pedido_list')

class PedidoCreateView(CreateView):
   model = Pedido
   form_class = PedidoCreateForm
   template_name = 'pedido_create.html'
   success_url = reverse_lazy('pedido_list')

   def get(self, request, *args, **kwargs):
      """
      Handles GET requests and instantiates blank versions of the form
      and its inline formsets.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      pedidoitem_form = PedidoItemCreateFormSet()
      return self.render_to_response(
         self.get_context_data(
            form=form,
            pedidoitem_form=pedidoitem_form,
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
      pedidoitem_form = PedidoItemCreateFormSet(self.request.POST)
      if (form.is_valid() and pedidoitem_form.is_valid()):
         return self.form_valid(form, pedidoitem_form)
      else:
         return self.form_invalid(form, pedidoitem_form)

   def form_valid(self, form, pedidoitem_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      self.object = form.save()
      pedidoitem_form.instance = self.object
      pedidoitem_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, pedidoitem_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      return self.render_to_response(
         self.get_context_data(
            form=form,
            pedidoitem_form=pedidoitem_form,
         )
      )