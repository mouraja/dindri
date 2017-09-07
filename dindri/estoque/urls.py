"""
dindri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from estoque.views import EstoqueHomeView
from estoque.views import EntradaListView, EntradaDetailView, EntradaCreateView, EntradaUpdateView, EntradaDeleteView
from estoque.views import SaidaListView, SaidaDetailView, SaidaCreateView, SaidaUpdateView, SaidaDeleteView
from estoque.views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, ItemActiveView
from estoque.views import CategoriaListView, CategoriaDetailView, CategoriaCreateView, CategoriaUpdateView, \
   CategoriaDeleteView, CategoriaActiveView

urlpatterns = [
   #  Home
   url(r'^$', EstoqueHomeView.as_view(), name='estoque_home'),
   #  Entrada
   url(r'^entrada/lista/$', EntradaListView.as_view(), name='entrada_list'),
   url(r'^entrada/novo/$', EntradaCreateView.as_view(), name='entrada_create'),
   url(r'^entrada/detalha(?P<pk>\d+)$', EntradaDetailView.as_view(), name='entrada_detail'),
   url(r'^entrada/edita/(?P<pk>\d+)$', EntradaUpdateView.as_view(), name='entrada_update'),
   url(r'^entrada/exclui/(?P<pk>\d+)$', EntradaDeleteView.as_view(), name='entrada_delete'),
   #  Saida
   url(r'^saida/lista/$', SaidaListView.as_view(), name='saida_list'),
   url(r'^saida/novo/$', SaidaCreateView.as_view(), name='saida_create'),
   url(r'^saida/detalha(?P<pk>\d+)$', SaidaDetailView.as_view(), name='saida_detail'),
   url(r'^saida/edita/(?P<pk>\d+)$', SaidaUpdateView.as_view(), name='saida_update'),
   url(r'^saida/exclui/(?P<pk>\d+)$', SaidaDeleteView.as_view(), name='saida_delete'),
   #  Item
   url(r'^item/lista/$', ItemListView.as_view(), name='item_list'),
   url(r'^item/novo/$', ItemCreateView.as_view(), name='item_create'),
   url(r'^item/detalha/(?P<pk>\d+)$', ItemDetailView.as_view(), name='item_detail'),
   url(r'^item/edita/(?P<pk>\d+)$', ItemUpdateView.as_view(), name='item_update'),
   url(r'^item/exclui/(?P<pk>\d+)$', ItemDeleteView.as_view(), name='item_delete'),
   url(r'^item/ativa/(?P<pk>\d+)$', ItemActiveView.as_view(), name='item_active'),
   #  Categoria
   url(r'^categoria/lista/$', CategoriaListView.as_view(), name='categoria_list'),
   url(r'^categoria/novo/$', CategoriaCreateView.as_view(), name='categoria_create'),
   url(r'^categoria/detalha/(?P<pk>\d+)$', CategoriaDetailView.as_view(), name='categoria_detail'),
   url(r'^categoria/edita/(?P<pk>\d+)$', CategoriaUpdateView.as_view(), name='categoria_update'),
   url(r'^categoria/exclui/(?P<pk>\d+)$', CategoriaDeleteView.as_view(), name='categoria_delete'),
   url(r'^categoria/ativa/(?P<pk>\d+)$', CategoriaActiveView.as_view(), name='categoria_active'),
]
