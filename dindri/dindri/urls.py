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
from django.conf.urls import url, include
from django.contrib import admin
from home import views as home_views

urlpatterns = [
   url(r'^$', home_views.home, name='home'),
   url(r'^relacionamento/', include('relacionamento.urls')),
   url(r'^vendas/', include('vendas.urls')),
   url(r'^compras/', include('compras.urls')),
   url(r'^estoque/', include('estoque.urls')),
   url(r'^producao/', include('producao.urls')),
   url(r'^receitas/', include('receitas.urls')),
   url(r'^admin/', admin.site.urls),
]
