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
from compras.views import ComprasHomeView
from compras.views import CompraListView, CompraDetailView, CompraCreateView
from compras.views import CompraDeleteView, CompraUpdateView, CompraDoneView, CompraCancelView
from compras.views import PedidoListView, PedidoDetailView, PedidoCreateView
from compras.views import PedidoDeleteView, PedidoUpdateView, PedidoActiveView
from compras.views import FornecedorListView, FornecedorDetailView, FornecedorCreateView
from compras.views import FornecedorDeleteView, FornecedorUpdateView, FornecedorActiveView

urlpatterns = [
   # Home
   url(r'^$', ComprasHomeView.as_view(), name='compras_home'),
   # Fornecedor
   url(r'^fornecedor/lista/$', FornecedorListView.as_view(), name='fornecedor_list'),
   url(r'^fornecedor/novo/$', FornecedorCreateView.as_view(), name='fornecedor_create'),
   url(r'^fornecedor/detalha/(?P<pk>\d+)$', FornecedorDetailView.as_view(), name='fornecedor_detail'),
   url(r'^fornecedor/edita/(?P<pk>\d+)$', FornecedorUpdateView.as_view(), name='fornecedor_update'),
   url(r'^fornecedor/exclui/(?P<pk>\d+)$', FornecedorDeleteView.as_view(), name='fornecedor_delete'),
   url(r'^fornecedor/ativa/(?P<pk>\d+)$', FornecedorActiveView.as_view(), name='fornecedor_active'),
   # Compra
   url(r'^compra/lista/$', CompraListView.as_view(), name='compra_list'),
   url(r'^compra/novo/$', CompraCreateView.as_view(), name='compra_create'),
   url(r'^compra/detalha/(?P<pk>\d+)$', CompraDetailView.as_view(), name='compra_detail'),
   url(r'^compra/edita/(?P<pk>\d+)$', CompraUpdateView.as_view(), name='compra_update'),
   url(r'^compra/exclui/(?P<pk>\d+)$', CompraDeleteView.as_view(), name='compra_delete'),
   url(r'^compra/conclui/(?P<pk>\d+)$', CompraDoneView.as_view(), name='compra_done'),
   url(r'^compra/cancela/(?P<pk>\d+)$', CompraCancelView.as_view(), name='compra_cancel'),
   # Pedido
   url(r'^pedido/lista/$', PedidoListView.as_view(), name='pedido_list'),
   url(r'^pedido/novo/$', PedidoCreateView.as_view(), name='pedido_create'),
   url(r'^pedido/detalha/(?P<pk>\d+)$', PedidoDetailView.as_view(), name='pedido_detail'),
   url(r'^pedido/edita/(?P<pk>\d+)$', PedidoUpdateView.as_view(), name='pedido_update'),
   url(r'^pedido/exclui/(?P<pk>\d+)$', PedidoDeleteView.as_view(), name='pedido_delete'),
   url(r'^pedido/ativa/(?P<pk>\d+)$', PedidoActiveView.as_view(), name='pedido_active'),
]