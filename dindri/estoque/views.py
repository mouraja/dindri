from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from estoque.models import Categoria, Item, Entrada, EntradaItem, Saida, SaidaItem
from estoque.forms import CategoriaCreateUpdateForm, CategoriaDetailForm, CategoriaDeleteForm, CategoriaActiveForm
from estoque.forms import ItemCreateUpdateForm, ItemDetailForm, ItemDeleteForm, ItemActiveForm
from estoque.forms import EntradaForm
from estoque.forms import SaidaForm


# Create your views here.

### Ambiente de producao
class EstoqueHomeView(TemplateView):
   template_name = 'estoque_home.html'


### Saida
class SaidaListView(ListView):
   model = Saida
   template_name = 'saida_list.html'
   fields = [
      'nome',
      'descricao',
   ]

   def get_queryset(self):
      qs = super(SaidaListView, self).get_queryset()
      qs = qs.filter(esta_excluido__exact=False)
      return qs


class SaidaDetailView(DetailView):
   model = Saida
   form_class = SaidaForm
   template_name = 'saida_detail.html'


class SaidaCreateView(CreateView):
   model = Saida
   form_class = SaidaForm
   template_name = 'saida_create.html'


class SaidaUpdateView(UpdateView):
   model = Saida
   form_class = SaidaForm
   template_name = 'saida_update.html'


class SaidaDeleteView(DeleteView):
   model = Saida
   form_class = SaidaForm
   template_name = 'saida_delete_confirm.html'


### Entrada
class EntradaListView(ListView):
   model = Entrada
   template_name = 'entrada_list.html'


class EntradaDetailView(DetailView):
   model = Entrada
   form_class = EntradaForm
   template_name = 'entrada_detail.html'


class EntradaCreateView(CreateView):
   model = Entrada
   form_class = EntradaForm
   template_name = 'entrada_create.html'


class EntradaUpdateView(UpdateView):
   model = Entrada
   form_class = EntradaForm
   template_name = 'entrada_update.html'


class EntradaDeleteView(DeleteView):
   model = Entrada
   form_class = EntradaForm
   template_name = 'entrada_delete_confirm.html'


### Item
class ItemListView(ListView):
   model = Item
   template_name = 'item_list.html'
   fields = [
      'nome',
      'descricao',
   ]

   def get_queryset(self):
      qs = super(ItemListView, self).get_queryset()
      qs = qs.filter(esta_excluido__exact=False)
      return qs


class ItemDetailView(DetailView):
   model = Item
   form_class = ItemDetailForm
   template_name = 'item_detail.html'
   success_url = reverse_lazy('item_list')


class ItemCreateView(CreateView):
   model = Item
   form_class = ItemCreateUpdateForm
   template_name = 'item_create.html'
   success_url = reverse_lazy('item_list')


class ItemUpdateView(UpdateView):
   model = Item
   form_class = ItemCreateUpdateForm
   template_name = 'item_update.html'
   success_url = reverse_lazy('item_list')


class ItemActiveView(UpdateView):
   model = Item
   form_class = ItemActiveForm
   template_name = 'item_active.html'
   success_url = reverse_lazy('item_list')


class ItemDeleteView(DeleteView):
   model = Item
   form_class = ItemDeleteForm
   template_name = 'item_delete_confirm.html'
   success_url = reverse_lazy('item_list')


### Categoria
class CategoriaListView(ListView):
   model = Categoria
   template_name = 'categoria_list.html'
   fields = (
      'nome',
      'descricao',
   )

   def get_queryset(self):
      qs = super(CategoriaListView, self).get_queryset()
      qs = qs.filter(esta_excluido__exact=False)
      return qs


class CategoriaDetailView(DetailView):
   model = Categoria
   form_class = CategoriaDetailForm
   template_name = 'categoria_detail.html'
   success_url = reverse_lazy('categoria_list')


class CategoriaCreateView(CreateView):
   model = Categoria
   form_class = CategoriaCreateUpdateForm
   template_name = 'categoria_create.html'
   success_url = reverse_lazy('categoria_list')


class CategoriaUpdateView(UpdateView):
   model = Categoria
   form_class = CategoriaCreateUpdateForm
   template_name = 'categoria_update.html'
   success_url = reverse_lazy('categoria_list')


class CategoriaActiveView(UpdateView):
   model = Categoria
   form_class = CategoriaActiveForm
   template_name = 'categoria_active.html'
   success_url = reverse_lazy('categoria_list')


class CategoriaDeleteView(DeleteView):
   model = Categoria
   form_class = CategoriaDeleteForm
   template_name = 'categoria_delete_confirm.html'
   success_url = reverse_lazy('categoria_list')
