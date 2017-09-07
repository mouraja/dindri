from django.db import models
from django.utils import timezone

from producao.models import Produto
from relacionamento.models import Cliente
from utils.models import Seguranca

# Create your models here.

VENDA_A_VAREJO = 1
VENDA_A_ATACADO = 2

TIPO_VENDA_CHOICES = (
   (VENDA_A_VAREJO, 'Venda no varejo'),
   (VENDA_A_ATACADO, 'Venda no atacado'),
)

ENTREGA_LOCAL = 1
ENTREGA_CONDOMINIO = 2
ENTREGA_EXTERNA = 3

TIPO_ENTREGA_CHOICES = (
   (ENTREGA_LOCAL, 'Entrega local'),
   (ENTREGA_CONDOMINIO, 'Entrega condominio'),
   (ENTREGA_EXTERNA, 'Entrega externa'),
)

PAGTO_A_VISTA = 1
PAGTO_A_PRAZO = 2
PAGTO_PARCELADO = 3

TIPO_PAGAMENTO_CHOICES = (
   (PAGTO_A_VISTA, 'À vista'),
   (PAGTO_A_PRAZO, 'A prazo'),
   (PAGTO_PARCELADO, 'Parcelado'),
)

PAGTO_EM_DINHEIRO = 1
PAGTO_EM_CHEQUE = 2
PAGTO_EM_CARTAO_CREDITO = 3
PAGTO_EM_CARTAO_DEBITO = 4

TIPO_FORMA_PAGAMENTO_CHOICES = (
   (PAGTO_EM_DINHEIRO, 'Em dinheiro'),
   (PAGTO_EM_CHEQUE, 'Em cheque'),
   (PAGTO_EM_CARTAO_DEBITO, 'Cartão débito'),
   (PAGTO_EM_CARTAO_CREDITO, 'Cartão crédito'),
)


class TipoContato(Seguranca):
   nome = models.CharField(max_length=150)
   descricao = models.TextField(max_length=500)

   def __str__(self):
      return self.nome


class Venda(Seguranca):
   data_venda = models.DateTimeField(default=timezone.now)
   tipo_venda = models.IntegerField(choices=TIPO_VENDA_CHOICES, default=1)
   cliente = models.ForeignKey(
      Cliente,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )
   valor_itens_total = models.DecimalField(max_digits=7, decimal_places=2, default=0)
   valor_itens_desconto = models.DecimalField(max_digits=7, decimal_places=2, default=0)
   valor_venda_subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=0)
   valor_venda_desconto = models.DecimalField(max_digits=7, decimal_places=2, default=0)
   valor_venda_total = models.DecimalField(max_digits=7, decimal_places=2, default=0)
   tipo_pagamento = models.IntegerField(choices=TIPO_PAGAMENTO_CHOICES, default=1)
   tipo_forma_pagamento = models.IntegerField(choices=TIPO_FORMA_PAGAMENTO_CHOICES, default=1)
   troco_para = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
   levar_troco = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
   tipo_entrega = models.IntegerField(choices=TIPO_ENTREGA_CHOICES, default=1)
   data_entrega = models.DateTimeField(auto_now_add=True, editable=True)
   esta_entregue = models.BooleanField(default=False)
   esta_pago = models.BooleanField(default=False)
   houve_devolucao = models.BooleanField(default=False)
   necessita_isopor = models.BooleanField(default=False)
   esta_concluida = models.BooleanField(default=False)
   motivo_desconto = models.TextField(max_length=300, null=True, blank=True)

   def is_venda_no_varejo(self):
      return self.tipo_venda == 1

   def is_venda_no_atacado(self):
      return self.tipo_venda == 1

      # def save(self):
      # sub_itens_total = 0
      # sub_itens_descontos = 0
      # sub_vendas_total = 0
      # itens = Venda_Produto.objects.filter(pk = self.pk)
      # for item in itens:
      # sub_itens_subtotal = sub_itens_subtotal + itens.subtotal
      # sub_itens_desconto = sub_itens_desconto + itens.desconto_total
      # self.valor_itens_subtotal = sub_itens_subtotal
      # self.valor_itens_desconto = sub_itens_desconto
      # self.valor_venda_subtotal = (sub_itens_subtotal - sub_itens_desconto) 

   def __str__(self):
      return "%s - %s" % (self.data_venda.strftime("%Y-%m-%d %H:%M:%S"), self.cliente.nome_preferencial)


class VendaProduto(models.Model):
   venda = models.ForeignKey(
      Venda,
      on_delete=models.CASCADE,
      limit_choices_to={'esta_concluida': False},
   )
   produto = models.ForeignKey(
      Produto,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )
   quantidade = models.IntegerField(default=0)

   def get_valor_custo(self):
      return self.produto.valor_custo_produto or 0.0

   valor_custo = property(get_valor_custo)

   def get_valor_minimo(self):
      preco = 0.0
      if self.produto.is_venda_no_varejo():
         preco = self.produto.preco_varejo_minimo
      if self.produto.is_venda_no_atacado():
         preco = self.produto.preco_atacado_minimo
      return preco

   valor_minimo = property(get_valor_minimo)

   def get_valor_unitario(self):
      preco = 0.0
      if self.venda.is_venda_no_varejo():
         preco = self.produto.preco_varejo_sugerido
      if self.venda.is_venda_no_atacado():
         preco = self.produto.preco_atacado_sugerido
      return preco

   valor_unitario = property(get_valor_unitario)

   valor_desconto_unitario = models.DecimalField(max_digits=5, decimal_places=2, default=0)

   def get_valor_subtotal(self):
      return (self.valor_unitario * self.quantidade)

   valor_subtotal = property(get_valor_subtotal)

   def get_valor_desconto_total(self):
      return (self.valor_desconto_unitario * self.quantidade)

   valor_desconto_total = property(get_valor_desconto_total)

   def get_valor_total(self):
      return (self.valor_subtotal - self.valor_desconto_total)

   valor_total = property(get_valor_total)

   def __str__(self):
      return "%s - %i - %f" % (self.produto.nome, self.quantidade, self.valor_total)


class Reposicao(Seguranca):
   data_reposicao = models.DateTimeField(default=timezone.now)
   qtde_reposta = models.IntegerField(default=0)
   custo_reposicao = models.DecimalField(max_digits=10, decimal_places=6, default=0)
   esta_concluida = models.BooleanField(default=False)

   def __str__(self):
      return self.data_reposicao.strftime("%Y-%m-%d %H:%M:%S")


class ReposicaoProduto(models.Model):
   reposicao = models.ForeignKey(
      Reposicao,
      on_delete=models.CASCADE,
      limit_choices_to={'esta_concluida': False},
   )
   produto = models.ForeignKey(
      Produto,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )
   quantidade = models.IntegerField(default=0)
   valor_custo_unitario = models.DecimalField(max_digits=9, decimal_places=6, default=0)

   def get_valor_custo_total(self):
      return (self.quantidade * self.valor_custo_unitario)

   valor_custo_total = property(get_valor_custo_total)

   def __str__(self):
      return "%s - %i - %f" % (self.produto.nome, self.quantidade, self.valor_custo_total)
