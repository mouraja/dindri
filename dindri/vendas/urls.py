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
from vendas.views import VendasHomeView, \
   TipoContatoListView, TipoContatoCreateView, TipoContatoDeleteView, TipoContatoDetailView, TipoContatoUpdateView, \
   VendaListView, VendaCreateView, VendaDeleteView, VendaDetailView, VendaUpdateView, \
   ReposicaoListView, ReposicaoCreateView, ReposicaoDeleteView, ReposicaoDetailView, ReposicaoUpdateView

urlpatterns = [
   ###  vendas
   url(r'^$', VendasHomeView.as_view(), name='vendas_home'),
   ###  venda
   url(r'^venda/lista/$', VendaListView.as_view(), name='venda_list'),
   url(r'^venda/novo/$', VendaCreateView.as_view(), name='venda_create'),
   url(r'^venda/detalha(?P<pk>\d+)$', VendaDetailView.as_view(), name='venda_detail'),
   url(r'^venda/edita/(?P<pk>\d+)$', VendaUpdateView.as_view(), name='venda_update'),
   url(r'^venda/exclui/(?P<pk>\d+)$', VendaDeleteView.as_view(), name='venda_delete'),
   ###  tipo_contato
   url(r'^tipo_contato/lista/$', TipoContatoListView.as_view(), name='tipo_contato_list'),
   url(r'^tipo_contato/novo/$', TipoContatoCreateView.as_view(), name='tipo_contato_create'),
   url(r'^tipo_contato/detalha(?P<pk>\d+)$', TipoContatoUpdateView.as_view(), name='tipo_contato_detail'),
   url(r'^tipo_contato/edita/(?P<pk>\d+)$', TipoContatoDetailView.as_view(), name='tipo_contato_update'),
   url(r'^tipo_contato/exclui/(?P<pk>\d+)$', TipoContatoDeleteView.as_view(), name='tipo_contato_delete'),
   ###  reposicao
   url(r'^reposicao/lista/$', ReposicaoListView.as_view(), name='reposicao_list'),
   url(r'^reposicao/novo/$', ReposicaoCreateView.as_view(), name='reposicao_create'),
   url(r'^reposicao/detalha(?P<pk>\d+)$', ReposicaoDeleteView.as_view(), name='reposicao_detail'),
   url(r'^reposicao/edita/(?P<pk>\d+)$', ReposicaoDetailView.as_view(), name='reposicao_update'),
   url(r'^reposicao/exclui/(?P<pk>\d+)$', ReposicaoUpdateView.as_view(), name='reposicao_delete'),
]
