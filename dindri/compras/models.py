from django.db import models
from django.utils import timezone
from utils.models import Seguranca, Endereco
from estoque.models import Categoria, Item

# Create your models here.

PEDIDO_PENDENTE = 'n'
PEDIDO_ABERTO = 'a'
PEDIDO_FECHADO = 'f'
PEDIDO_CANCELADO = 'c'
PEDIDO_EXCLUIDO = 'e'

SITUACAO_PEDIDO_CHOICES = (
   (PEDIDO_PENDENTE, 'Pedido pendente'),
   (PEDIDO_ABERTO, 'Pedido em aberto'),
   (PEDIDO_FECHADO, 'Pedido fechado'),
   (PEDIDO_CANCELADO, 'Pedido cancelado'),
   (PEDIDO_EXCLUIDO, 'Pedido excluído'),
)

COMPRA_PENDENTE = 'n'
COMPRA_ABERTA = 'a'
COMPRA_FECHADA = 'f'
COMPRA_PARCIAL = 'p'
COMPRA_CANCELADA = 'c'
COMPRA_EXCLUIDA = 'e'

SITUACAO_COMPRA_CHOICES = (
   (COMPRA_PENDENTE, 'Compra pendente'),
   (COMPRA_ABERTA, 'Compra em aberto'),
   (COMPRA_FECHADA, 'Compra fechada'),
   (COMPRA_PARCIAL, 'Compra atendida parcialmente'),
   (COMPRA_CANCELADA, 'Compra cancelada'),
   (COMPRA_EXCLUIDA, 'Compra excluída'),
)

FORNECEDOR_INSUMO = 1
FORNECEDOR_SERVICO = 2
FORNECEDOR_EMBALAGENS = 3

TIPO_FORNECEDOR_CHOICES = {
   (FORNECEDOR_INSUMO, 'Fornecedor de insumos'),
   (FORNECEDOR_SERVICO, 'Fornecedor de serviços'),
   (FORNECEDOR_EMBALAGENS, 'Fornecedor de embalagens'),
}

ITEM_PENDENTE = 'n'
ITEM_ATENDIDO = 'a'
ITEM_CANCELADO = 'c'
ITEM_EXCLUIDO = 'e'

SITUACAO_ITEM_PEDIDO_CHOICES = (
   (ITEM_PENDENTE, 'Item pendente'),
   (ITEM_ATENDIDO, 'Item atendido'),
   (ITEM_CANCELADO, 'Item cancelado'),
   (ITEM_EXCLUIDO, 'Item excluído'),
)

SITUACAO_ITEM_COMPRA_CHOICES = (
   (ITEM_PENDENTE, 'Item pendente'),
   (ITEM_ATENDIDO, 'Item atendido'),
   (ITEM_CANCELADO, 'Item cancelado'),
   (ITEM_EXCLUIDO, 'Item excluído'),
)

class Pedido(Seguranca):
   data_emissao = models.DateField(
      auto_now_add=True,
   )
   data_pedido = models.DateField(
      null=True,
      blank=True,
   )
   data_finalizado = models.DateField(
      null=True,
      blank=True,
   )
   data_limite = models.DateField(
      null=True,
      blank=True,
   )
   situacao_pedido = models.CharField(
      max_length=1,
      choices=SITUACAO_PEDIDO_CHOICES,
      default=PEDIDO_PENDENTE,
   )
   situacao_compra = models.CharField(
      max_length=1,
      choices=SITUACAO_COMPRA_CHOICES,
      default=COMPRA_PENDENTE,
   )
   solicitante = models.CharField(
      max_length=256,
   )
   observacao = models.TextField(
      max_length=1024,
      null=True,
      blank=True,
   )

   def get_situacao_compra_descricao(self):
      for cod, desc in SITUACAO_COMPRA_CHOICES:
         if cod == self.situacao_compra:
            return desc
      return None

   def get_situacao_pedido_descricao(self):
      for cod, desc in SITUACAO_PEDIDO_CHOICES:
         if cod == self.situacao_pedido:
            return desc
      return None

   def __str__(self):
      return "%i - %s - %s" % (self.id, str(self.data_limite), self.solicitante)

class PedidoItem(Seguranca):
   pedido = models.ForeignKey(
      Pedido,
      on_delete=models.CASCADE,
      limit_choices_to={'esta_ativo': True}
   )
   item = models.ForeignKey(
      Categoria,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
      null=True,
      blank=True,
   )
   descricao = models.TextField(
      max_length=512,
      null=True,
      blank=True,
   )
   quantidade = models.PositiveIntegerField(
      default=0,
   )
   situacao_item = models.CharField(
      max_length=1,
      choices=SITUACAO_ITEM_PEDIDO_CHOICES,
      default=ITEM_PENDENTE,
   )

   def __str__(self):
      return "%s - %i" % (self.tipo_insumo.nome, self.quantidade)

class Fornecedor(Seguranca, Endereco):
   tipo_fornecedor = models.PositiveSmallIntegerField(
      choices=TIPO_FORNECEDOR_CHOICES,
      default=FORNECEDOR_INSUMO,
   )
   nome = models.CharField(
      max_length=256,
   )
   observacao = models.TextField(
      max_length=512,
      null=True,
      blank=True,
   )
   nome_fantasia = models.CharField(
      max_length=128,
      null=True,
      blank=True,
   )
   telefone = models.CharField(
      max_length=18,
      null=True,
      blank=True,
   )
   contato = models.CharField(
      max_length=256,
      null=True,
      blank=True,
   )
   email = models.EmailField(
      max_length=256,
      null=True,
      blank=True,
   )
   cnpj = models.CharField(
      max_length=14,
      null=True,
      blank=True,
   )

   def get_absolute_url(self):
      return 'fornecedor_list'

   def delete(self, *args, **kwargs):
      self.excluir()
      super(Fornecedor, self).save(*args, **kwargs)
      return

   def __str__(self):
      return "%i - %s" % (self.id, self.nome)

class Compra(Seguranca):
   fornecedor = models.ForeignKey(
      Fornecedor,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
      null=True,
   )
   '''
   pedido = models.ManyToManyField(
      Pedido,
      limit_choices_to={'esta_ativo': True},
      null=True,
   )
   '''
   nota_fiscal = models.CharField(
      max_length=64,
      null=True,
      blank=True,
   )
   data_emissao = models.DateTimeField(
      auto_now_add=True,
   )
   data_compra = models.DateTimeField(
      null=True,
      blank=True,
   )
   valor_total = models.DecimalField(
      max_digits=9,
      decimal_places=2,
      default=0.0,
   )
   situacao_compra = models.CharField(
      max_length=1,
      choices=SITUACAO_COMPRA_CHOICES,
      default=COMPRA_PENDENTE,
   )

   def get_situacao_compra_descricao(self):
      for cod, desc in SITUACAO_COMPRA_CHOICES:
         if cod == self.situacao_compra:
            return desc
      return None

   def cancelar(self):
      self.desativar()
      self.situacao_compra = COMPRA_CANCELADA

   def concluir(self, situacao=COMPRA_FECHADA):
      self.esta_ativo = False
      self.ativado_em = timezone.now()
      self.situacao_compra = situacao

   def remove_valor(self, valor=0):
      self.valor_total = self.valor_total - valor

   def add_valor(self, valor=0):
      self.valor_total = self.valor_total + valor

   def get_absolute_url(self):
      return 'compra_list'

   def save(self, *args, **kwargs):
      #compra = super(Compra, self).save(*args, **kwargs)
      if self.situacao_compra in [COMPRA_FECHADA, COMPRA_PARCIAL]:
         itens = self.compraitem_set.all().exclude(situacao_item__exact=ITEM_CANCELADO)
         self.valort_total = 0
         for item in itens:
            item.situacao_item = ITEM_ATENDIDO
            item.desativar()
            self.valor_total += item.valor_total
            item.save()
      return super(Compra, self).save(*args, **kwargs)

   def delete(self, *args, **kwargs):
      itens = self.compraitem_set.all()
      for item in itens.filter(situacao_item__exact=ITEM_PENDENTE):
         item.delete()
      if itens.filter(situacao_item__exact=ITEM_ATENDIDO).count() == 0:
         self.excluir()
      else:
         self.situacao_compra = COMPRA_PARCIAL
         self.cancelar()
      self.save()

      super(Compra, self).save(*args, **kwargs)
      return

   def __str__(self):
      return "%i - %s - %f" % (self.id, str(self.data_emissao), self.valor_total)

class CompraItem(Seguranca):

   __original = None

   compra = models.ForeignKey(
      Compra,
      on_delete=models.CASCADE,
   )
   item = models.ForeignKey(
      Item,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )
   quantidade = models.PositiveIntegerField(
      default=0,
   )
   valor_unitario = models.DecimalField(
      max_digits=9,
      decimal_places=2,
      default=0.0,
   )
   valor_total = models.DecimalField(
      max_digits=12,
      decimal_places=2,
      default=0.0,
   )
   situacao_item = models.CharField(
      max_length=1,
      choices=SITUACAO_ITEM_COMPRA_CHOICES,
      default=ITEM_PENDENTE,
   )

   def __init__(self, *args, **kwargs):
      super(CompraItem, self).__init__(*args, **kwargs)
      self.__original = self

   def calcule(self):
      self.valor_total = self.valor_unitario * self.quantidade

   def cancelar(self):
      self.desativar()
      self.situacao_item = ITEM_CANCELADO

   def atender(self):
      self.esta_ativo = False
      self.ativado_em = timezone.now()
      self.situacao_item = ITEM_ATENDIDO
      self.item.data_ultima_compra = self.ativado_em
      self.item.quantidade = self.item.quantidade + self.quantidade
      self.item.save()

   def is_cancelado(self):
      return self.situacao_item == ITEM_CANCELADO

   def is_pendente(self):
      return self.situacao_item == ITEM_PENDENTE

   def is_novo(self):
      return self.pk is None

   def is_valor_total_changed(self):
      return self.__original.valor_total != self.valor_total

   def save(self, *args, **kwargs):
      self.calcule()
      if self.is_novo():
         self.compra.add_valor(self.valor_total)
      else:
         if self.__original.esta_aberto:
            if self.is_valor_total_changed():
               self.compra.remove_valor(self._original.valor_total)
               self.compra.add_valor(self.valor_total)
            if self.is_cancelado():
               self.compra.remove_valor(self.valor_total)
            if self.is_pendente():
               self.atender()
      self.compra.save()
      return super(CompraItem, self).save(*args, **kwargs)

   def delete(self, *args, **kwargs):
      if not self.is_ativo():
         self.compra.remove_valor(self.valor_total)
         self.cancelar()
         self.excluir()
         super(CompraItem, self).save(*args, **kwargs)
      return

   def get_absolute_url(self):
      return 'compra_item_list'

   def __str__(self):
      return "%s - %i - %f" % (self.item.nome, self.quantidade, self.valor_total)