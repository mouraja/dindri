"""dindri URL Configuration

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
from producao.views import ProducaoHomeView
from producao.views import InsumoListView, InsumoDetailView, InsumoCreateView, InsumoUpdateView, InsumoDeleteView
from producao.views import LoteBaseListView, LoteBaseDetailView, LoteBaseCreateView, LoteBaseUpdateView, \
   LoteBaseDeleteView
from producao.views import LoteSaborListView, LoteSaborDetailView, LoteSaborCreateView, LoteSaborUpdateView, \
   LoteSaborDeleteView
from producao.views import LoteProdutoListView, LoteProdutoDetailView, LoteProdutoCreateView, LoteProdutoUpdateView, \
   LoteProdutoDeleteView
from producao.views import TipoBaseListView, TipoBaseDetailView, TipoBaseCreateView, TipoBaseUpdateView, \
   TipoBaseDeleteView, TipoBaseActiveView
from producao.views import TipoSaborListView, TipoSaborDetailView, TipoSaborCreateView, TipoSaborUpdateView, \
   TipoSaborDeleteView, TipoSaborActiveView
from producao.views import TipoProdutoListView, TipoProdutoDetailView, TipoProdutoCreateView, TipoProdutoUpdateView, \
   TipoProdutoDeleteView, TipoProdutoActiveView
from producao.views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView
from producao.views import SaborListView, SaborDetailView, SaborCreateView, SaborUpdateView, SaborDeleteView
from producao.views import ProdutoListView, ProdutoDetailView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
   ###  home
   url(r'^$', ProducaoHomeView.as_view(), name='producao_home'),
   ###  insumo 
   url(r'^insumo/lista/$', InsumoListView.as_view(), name='insumo_list'),
   url(r'^insumo/novo/$', InsumoCreateView.as_view(), name='insumo_create'),
   url(r'^insumo/detalha(?P<pk>\d+)$', InsumoDetailView.as_view(), name='insumo_detail'),
   url(r'^insumo/edita/(?P<pk>\d+)$', InsumoUpdateView.as_view(), name='insumo_update'),
   url(r'^insumo/exclui/(?P<pk>\d+)$', InsumoDeleteView.as_view(), name='insumo_delete'),
   ###  lote_base
   url(r'^lote_base/lista/$', LoteBaseListView.as_view(), name='lote_base_list'),
   url(r'^lote_base/novo/$', LoteBaseCreateView.as_view(), name='lote_base_create'),
   url(r'^lote_base/detalha(?P<pk>\d+)$', LoteBaseDetailView.as_view(), name='lote_base_detail'),
   url(r'^lote_base/edita/(?P<pk>\d+)$', LoteBaseUpdateView.as_view(), name='lote_base_update'),
   url(r'^lote_base/exclui/(?P<pk>\d+)$', LoteBaseDeleteView.as_view(), name='lote_base_delete'),
   ###  lote_sabor
   url(r'^lote_sabor/lista/$', LoteSaborListView.as_view(), name='lote_sabor_list'),
   url(r'^lote_sabor/novo/$', LoteSaborCreateView.as_view(), name='lote_sabor_create'),
   url(r'^lote_sabor/detalha(?P<pk>\d+)$', LoteSaborDetailView.as_view(), name='lote_sabor_detail'),
   url(r'^lote_sabor/edita/(?P<pk>\d+)$', LoteSaborUpdateView.as_view(), name='lote_sabor_update'),
   url(r'^lote_sabor/exclui/(?P<pk>\d+)$', LoteSaborDeleteView.as_view(), name='lote_sabor_delete'),
   ###  lote_produto
   url(r'^lote_produto/lista/$', LoteProdutoListView.as_view(), name='lote_produto_list'),
   url(r'^lote_produto/novo/$', LoteProdutoCreateView.as_view(), name='lote_produto_create'),
   url(r'^lote_produto/detalha(?P<pk>\d+)$', LoteProdutoDetailView.as_view(), name='lote_produto_detail'),
   url(r'^lote_produto/edita/(?P<pk>\d+)$', LoteProdutoUpdateView.as_view(), name='lote_produto_update'),
   url(r'^lote_produto/exclui/(?P<pk>\d+)$', LoteProdutoDeleteView.as_view(), name='lote_produto_delete'),
   ###  tipo_base
   url(r'^tipo_base/lista/$', TipoBaseListView.as_view(), name='tipo_base_list'),
   url(r'^tipo_base/novo/$', TipoBaseCreateView.as_view(), name='tipo_base_create'),
   url(r'^tipo_base/detalha/(?P<pk>\d+)$', TipoBaseDetailView.as_view(), name='tipo_base_detail'),
   url(r'^tipo_base/edita/(?P<pk>\d+)$', TipoBaseUpdateView.as_view(), name='tipo_base_update'),
   url(r'^tipo_base/exclui/(?P<pk>\d+)$', TipoBaseDeleteView.as_view(), name='tipo_base_delete'),
   url(r'^tipo_base/ativa/(?P<pk>\d+)$', TipoBaseActiveView.as_view(), name='tipo_base_active'),
   ###  tipo_sabor
   url(r'^tipo_sabor/lista/$', TipoSaborListView.as_view(), name='tipo_sabor_list'),
   url(r'^tipo_sabor/novo/$', TipoSaborCreateView.as_view(), name='tipo_sabor_create'),
   url(r'^tipo_sabor/detalha/(?P<pk>\d+)$', TipoSaborDetailView.as_view(), name='tipo_sabor_detail'),
   url(r'^tipo_sabor/edita/(?P<pk>\d+)$', TipoSaborUpdateView.as_view(), name='tipo_sabor_update'),
   url(r'^tipo_sabor/exclui/(?P<pk>\d+)$', TipoSaborDeleteView.as_view(), name='tipo_sabor_delete'),
   url(r'^tipo_sabor/ativa/(?P<pk>\d+)$', TipoSaborActiveView.as_view(), name='tipo_sabor_active'),
   ###  tipo_produto
   url(r'^tipo_produto/lista/$', TipoProdutoListView.as_view(), name='tipo_produto_list'),
   url(r'^tipo_produto/novo/$', TipoProdutoCreateView.as_view(), name='tipo_produto_create'),
   url(r'^tipo_produto/detalha/(?P<pk>\d+)$', TipoProdutoDetailView.as_view(), name='tipo_produto_detail'),
   url(r'^tipo_produto/edita/(?P<pk>\d+)$', TipoProdutoUpdateView.as_view(), name='tipo_produto_update'),
   url(r'^tipo_produto/exclui/(?P<pk>\d+)$', TipoProdutoDeleteView.as_view(), name='tipo_produto_delete'),
   url(r'^tipo_produto/ativa/(?P<pk>\d+)$', TipoProdutoActiveView.as_view(), name='tipo_produto_active'),
   ###  base
   url(r'^base/lista/$', BaseListView.as_view(), name='base_list'),
   url(r'^base/novo/$', BaseCreateView.as_view(), name='base_create'),
   url(r'^base/detalha(?P<pk>\d+)$', BaseDetailView.as_view(), name='base_detail'),
   url(r'^base/edita/(?P<pk>\d+)$', BaseUpdateView.as_view(), name='base_update'),
   url(r'^base/exclui/(?P<pk>\d+)$', BaseDeleteView.as_view(), name='base_delete'),
   ###  sabor
   url(r'^sabor/lista/$', SaborListView.as_view(), name='sabor_list'),
   url(r'^sabor/novo/$', SaborCreateView.as_view(), name='sabor_create'),
   url(r'^sabor/detalha/(?P<pk>\d+)$', SaborDetailView.as_view(), name='sabor_detail'),
   url(r'^sabor/edita/(?P<pk>\d+)$', SaborUpdateView.as_view(), name='sabor_update'),
   url(r'^sabor/exclui/(?P<pk>\d+)$', SaborDeleteView.as_view(), name='sabor_delete'),
   ###  produto
   url(r'^produto/lista/$', ProdutoListView.as_view(), name='produto_list'),
   url(r'^produto/novo/$', ProdutoCreateView.as_view(), name='produto_create'),
   url(r'^produto/detalha(?P<pk>\d+)$', ProdutoDetailView.as_view(), name='produto_detail'),
   url(r'^produto/edita/(?P<pk>\d+)$', ProdutoUpdateView.as_view(), name='produto_update'),
   url(r'^produto/exclui/(?P<pk>\d+)$', ProdutoDeleteView.as_view(), name='produto_delete'),
]
