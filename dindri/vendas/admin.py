from django.contrib import admin
from vendas.models import TipoContato, Venda, VendaProduto, Reposicao, ReposicaoProduto


class VendaProdutoInline(admin.TabularInline):
   # readonly_fields = ('preco_unitario','desconto_total','preco_total',)
   model = VendaProduto


class VendaAdmin(admin.ModelAdmin):
   # readonly_fields = ('valor_produtos','desconto_produtos','valor_total',)
   inlines = [VendaProdutoInline]


class ReposicaoProdutoInline(admin.TabularInline):
   # readonly_fields = ('custo_total',)
   model = ReposicaoProduto


class ReposicaoAdmin(admin.ModelAdmin):
   # readonly_fields = ('qtde_reposta','custo_reposicao',)
   inlines = [ReposicaoProdutoInline]


# Register your models here.

admin.site.register(TipoContato)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Reposicao, ReposicaoAdmin)
