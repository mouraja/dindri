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
from relacionamento.views import RelacionamentoHomeView, \
   ClienteCreateView, ClienteDetailView, ClienteListView, ClienteUpdateView, ClienteDeleteView, \
   ClienteActiveView, ClienteBlockView

urlpatterns = [
   # Relacionamento
   url(r'^$', RelacionamentoHomeView.as_view(), name='relacionamento_home'),
   # Cliente
   url(r'^cliente/lista/$', ClienteListView.as_view(), name='cliente_list'),
   url(r'^cliente/novo/$', ClienteCreateView.as_view(), name='cliente_create'),
   url(r'^cliente/detalha/(?P<pk>\d+)$', ClienteDetailView.as_view(), name='cliente_detail'),
   url(r'^cliente/edita/(?P<pk>\d+)$', ClienteUpdateView.as_view(), name='cliente_update'),
   url(r'^cliente/exclui/(?P<pk>\d+)$', ClienteDeleteView.as_view(), name='cliente_delete'),
   url(r'^cliente/ativa/(?P<pk>\d+)$', ClienteActiveView.as_view(), name='cliente_active'),
   url(r'^cliente/bloqueia/(?P<pk>\d+)$', ClienteBlockView.as_view(), name='cliente_block'),
]
