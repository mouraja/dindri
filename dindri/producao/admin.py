from django.contrib import admin
from producao.models import TipoProduto, TipoBase, TipoSabor
from producao.models import LoteProduto, LoteBase, LoteSabor
from producao.models import Produto, ProdutoInsumo, ProdutoSabor
from producao.models import Base, BaseInsumo, Insumo
from producao.models import Sabor, SaborInsumo, SaborBase


# Register your models here.

class ProdutoSaborInline(admin.TabularInline):
   # readonly_fields = ('preco_unitario','desconto_total','preco_total',)
   model = ProdutoSabor


class ProdutoInsumoInline(admin.TabularInline):
   # readonly_fields = ('preco_unitario','desconto_total','preco_total',)
   model = ProdutoInsumo


class ProdutoAdmin(admin.ModelAdmin):
   # readonly_fields = ('valor_produtos','desconto_produtos','valor_total',)
   inlines = [ProdutoSaborInline, ProdutoInsumoInline]


class SaborBaseInline(admin.TabularInline):
   # readonly_fields = ('custo_total',)
   model = SaborBase


class SaborInsumoInline(admin.TabularInline):
   # readonly_fields = ('custo_total',)
   model = SaborInsumo


class SaborAdmin(admin.ModelAdmin):
   # readonly_fields = ('qtde_reposta','custo_reposicao',)
   inlines = [SaborBaseInline, SaborInsumoInline]


class BaseInsumoInline(admin.TabularInline):
   # readonly_fields = ('custo_total',)
   model = BaseInsumo


class BaseAdmin(admin.ModelAdmin):
   # readonly_fields = ('qtde_reposta','custo_reposicao',)
   inlines = [BaseInsumoInline]


# Register your models here.

admin.site.register(LoteBase)
admin.site.register(LoteSabor)
admin.site.register(LoteProduto)

admin.site.register(TipoBase)
admin.site.register(TipoSabor)
admin.site.register(TipoProduto)

admin.site.register(Insumo)

admin.site.register(Base, BaseAdmin)
admin.site.register(Sabor, SaborAdmin)
admin.site.register(Produto, ProdutoAdmin)
