from django.contrib import admin
from receitas.models import Receita, ReceitaIngrediente

'''
class Venda_Produto_Inline(admin.TabularInline):
   #readonly_fields = ('preco_unitario','desconto_total','preco_total',)
   model = Venda_Produto

class Venda_Admin(admin.ModelAdmin):
   #readonly_fields = ('valor_produtos','desconto_produtos','valor_total',)
   inlines = [Venda_Produto_Inline]

class Reposicao_Produto_Inline(admin.TabularInline):
   #readonly_fields = ('custo_total',)
   model = Reposicao_Produto

class Reposicao_Admin(admin.ModelAdmin):
   #readonly_fields = ('qtde_reposta','custo_reposicao',)
   inlines = [Reposicao_Produto_Inline]
'''

# Register your models here.

admin.site.register(Receita)
admin.site.register(ReceitaIngrediente)
