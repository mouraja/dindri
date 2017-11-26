from django.db import models
from utils.models import Seguranca, Restricao

UNIDADE_GRAMA='g'
UNIDADE_KILOGRAMA='Kg'
UNIDADE_LITRO='l'
UNIDADE_MILILITRO='ml'

UNIDADES_MEDIDAS_CHOICES=(
   (UNIDADE_GRAMA,'Grama'),
   (UNIDADE_MILILITRO,'Mililitro'),
   (UNIDADE_KILOGRAMA,'Kilograma'),
   (UNIDADE_LITRO,'Litro'),
)

class Categoria(Seguranca, Restricao):
   '''Categoria dos itens estocados'''
   nome = models.CharField(
      max_length=100,
   )
   descricao = models.TextField(
      max_length=500,
   )

   def get_absolute_url(self):
      return 'categoria_list'

   def save(self, *args, **kwargs):
      self.restringir()
      return super(Categoria, self).save(*args, **kwargs)

   def delete(self, *args, **kwargs):
      self.excluir()
      super(Categoria, self).save(*args, **kwargs)
      return

   def __str__(self):
      return "%i - %s" % (self.id, self.nome)

class Item(Seguranca, Restricao):
   '''Itens estocados'''
   categoria = models.ForeignKey(
      Categoria,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )
   nome = models.CharField(
      max_length=150,
   )
   descricao = models.TextField(
      max_length=512,
   )
   volume_unitario = models.PositiveIntegerField(
      default=0,
   )
   unidade = models.CharField(
      max_length=2,
      choices=UNIDADES_MEDIDAS_CHOICES,
      default=UNIDADE_GRAMA,
   )
   quantidade = models.PositiveIntegerField(
      default=0,
   )
   valor_custo_ultima_compra = models.DecimalField(
      max_digits=9,
      decimal_places=2,
      default=0.0,
   )
   valor_custo_medio = models.DecimalField(
      max_digits=12,
      decimal_places=6,
      default=0.0,
   )
   codigo_barra=models.CharField(
      max_length=14,
      null=True,
      blank=True,
   )
   data_ultima_compra = models.DateField(
      null=True,
      blank=True,
   )
   data_ultima_requisicao = models.DateField(
      null=True,
      blank=True,
   )

   def get_valor_custo_ml(self):
      return (self.valor_custo_ultima_compra / self.volume_unitario)

   valor_custo_ml = property(get_valor_custo_ml)

   def get_valor_custo_medio_ml(self):
      return (self.valor_custo_medio / self.volume_unitario)

   valor_custo_medio_ml = property(get_valor_custo_medio_ml)

   def get_absolute_url(self):
      return 'item_list'

   def save(self, *args, **kwargs):
      self.restringir()
      return super(Item, self).save(*args, **kwargs)

   def delete(self, *args, **kwargs):
      self.excluir()
      super(Item, self).save(*args, **kwargs)
      return

   def __str__(self):
      return "%i - %s" % (self.id, self.nome)

class Entrada(Seguranca):
   '''Entradas oriundas das compras'''
   data_entrada = models.DateField()
   valor_custo_total = models.DecimalField(
      max_digits=9,
      decimal_places=2,
      default=0.0,
   )

   # compra = models.ForeignKey(
   # Compra,
   # on_delete=models.SET_NULL,
   # limit_choices_to={'esta_ativo': True},
   # null=True,
   # blank=True,
   # )

   def __str__(self):
      return "%s - %i - %f" % (str(self.data_entrada), self.fornecedor, self.valor_custo_total)

class EntradaItem(models.Model):
   '''Entradas de itens no estoque'''
   entrada = models.ForeignKey(
      Entrada,
      on_delete=models.CASCADE,
   )
   item = models.ForeignKey(
      Item,
      on_delete=models.PROTECT,
   )
   quantidade = models.PositiveIntegerField()
   valor_custo_unitario = models.DecimalField(
      max_digits=12,
      decimal_places=4,
      default=0.0,
   )

   def get_valor_custo_total(self):
      return (self.quantidade * self.valor_custo_unitario)

   valor_custo_total = property(get_valor_custo_total)

   def __str__(self):
      return "%s - $i - %f" % (self.item.nome, self.quantidadde, self.valor_custo_total)

class Saida(Seguranca):
   '''Saidas efetuadas no estoque'''
   data_saida = models.DateField()
   valor_custo_total = models.DecimalField(
      max_digits=12,
      decimal_places=6,
      default=0.0,
   )

   def __str__(self):
      return "%s - %i - %f" % (str(self.data_saida), self.valor_custo_total)

class SaidaItem(models.Model):
   '''Saidas de itens do estoque'''
   saida = models.ForeignKey(
      Saida,
      on_delete=models.CASCADE,
   )
   item = models.ForeignKey(
      Item,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )
   quantidade = models.PositiveIntegerField()
   valor_custo_unitario = models.DecimalField(
      max_digits=12,
      decimal_places=6,
      default=0.0,
   )

   def get_valor_custo_total(self):
      return (self.quantidade * self.valor_custo_unitario)

   valor_custo_total = property(get_valor_custo_total)

   def __str__(self):
      return "%s - $i - %f" % (self.item.nome, self.quantidadde, self.valor_custo_total)
