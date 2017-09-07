from django.contrib import admin
from relacionamento.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
   model = Cliente
   list_display = ('nome_preferencial', 'watsapp')
   list_filter = ('nome_preferencial',)
   search_fields = ('nome_preferencial', 'watsapp', 'endereco')


# Register your models here.

admin.site.register(Cliente, ClienteAdmin)
