from django.contrib import admin
from compras.models import Fornecedor, Compra, CompraItem, Pedido, PedidoItem


class PedidoItemInline(admin.TabularInline):
   # readonly_fields = ('preco_unitario','desconto_total','preco_total',)
   model = PedidoItem


class PedidoAdmin(admin.ModelAdmin):
   # readonly_fields = ('valor_produtos','desconto_produtos','valor_total',)
   inlines = [PedidoItemInline]


class CompraItemInline(admin.TabularInline):
   # readonly_fields = ('custo_total',)
   model = CompraItem


class CompraAdmin(admin.ModelAdmin):
   # readonly_fields = ('qtde_reposta','custo_reposicao',)
   inlines = [CompraItemInline]


# Register your models here.

admin.site.register(Fornecedor)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Compra, CompraAdmin)
