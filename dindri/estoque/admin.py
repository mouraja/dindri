from django.contrib import admin
from estoque.models import Categoria, Item, Entrada, EntradaItem, Saida, SaidaItem


class EntradaItemInline(admin.TabularInline):
   # readonly_fields = ('preco_unitario','desconto_total','preco_total',)
   model = EntradaItem


class EntradaAdmin(admin.ModelAdmin):
   # readonly_fields = ('valor_produtos','desconto_produtos','valor_total',)
   inlines = [EntradaItemInline]


class SaidaItemInline(admin.TabularInline):
   # readonly_fields = ('custo_total',)
   model = SaidaItem


class SaidaAdmin(admin.ModelAdmin):
   # readonly_fields = ('qtde_reposta','custo_reposicao',)
   inlines = [SaidaItemInline]


# Register your models here.

admin.site.register(Item)
admin.site.register(Categoria)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Saida, SaidaAdmin)
