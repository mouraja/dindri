from django.utils import timezone
from django.db import models
from utils.models import Seguranca, Restricao
from estoque.models import Item


# Create your models here.

class Insumo(Seguranca, Restricao):
   produto = models.ForeignKey(
      Item,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )
   volume = models.PositiveIntegerField()
   valor_custo_medida = models.DecimalField(
      max_digits=12,
      decimal_places=6,
      default=0.0,
   )
   valor_custo_medio_medida = models.DecimalField(
      max_digits=12,
      decimal_places=6,
      default=0.0,
   )

   def get_absolute_url(self):
      return 'insumo_list'

   def save(self, *args, **kwargs):
      self.restringir()
      return super(Insumo, self).save(*args, **kwargs)

   def delete(self, *args, **kwargs):
      self.excluir()
      super(Insumo, self).save(*args, **kwargs)
      return

   def __str__(self):
      return "%i - %s" % (self.id, self.nome)


class LoteCusto(Seguranca, Restricao):
   data_producao = models.DateTimeField(
      auto_now_add=True,
   )
   data_producao_finalizada = models.DateTimeField(
      null=True,
      blank=True,
   )
   data_ultimo_consumo = models.DateTimeField(
      null=True,
      blank=True,
   )
   data_ultimo_descarte = models.DateTimeField(
      null=True,
      blank=True,
   )
   esta_finalizado = models.BooleanField(
      default=False,
   )
   volume_produzido = models.PositiveIntegerField(
      default=0,
   )
   volume_consumido = models.PositiveIntegerField(
      default=0,
   )
   volume_descartada = models.PositiveIntegerField(
      default=0,
   )

   def get_volume_estoque(self):
      return (self.volume_produzido - (self.volume_consumido + self.volume_descartado))

   volume_estoque = property(get_volume_estoque)

   valor_custo_volume_total = models.DecimalField(
      max_digits=12,
      decimal_places=6,
      default=0.0,
   )

   def get_valor_custo_volume_ml(self):
      return (self.valor_custo_volume_total / self.volume_produzido)

   valor_custo_volume_ml = property(get_valor_custo_volume_ml)

   quantidade_dindin_produzido = models.PositiveIntegerField(
      default=0,
   )

   def get_valor_custo_volume_por_dindin(self):
      return (self.valor_custo_volume_total / self.quantidade_dindin_produzido)

   valor_custo_volume_por_dindin = property(get_valor_custo_volume_por_dindin)

   def get_rendimento_volume_por_dindin(self):
      return (self.volume_produzido / self.quantidade_dindin_produzido)

   rendimento_volume_por_dindin = property(get_rendimento_volume_por_dindin)

   class Meta:
      abstract = True


class BaseCusto(Seguranca, Restricao):
   nome = models.CharField(max_length=150)
   descricao = models.TextField(max_length=512)
   data_producao = models.DateTimeField(
      auto_now_add=True,
      editable=True,
   )
   data_producao_finalizada = models.DateTimeField(
      auto_now_add=True,
      editable=True,
   )
   esta_finalizada = models.BooleanField(
      default=False,
   )
   volume_produzido = models.PositiveIntegerField()
   volume_consumido = models.PositiveIntegerField(
      default=0,
   )
   volume_descartado = models.PositiveIntegerField(
      default=0,
   )

   def get_volume_estoque(self):
      return (self.volume_produzido - (self.volume_consumido + self.volume_descartado))

   volume_estoque = property(get_volume_estoque)

   valor_custo_operacional = models.DecimalField(
      max_digits=9,
      decimal_places=6,
      default=0.0
   )
   valor_custo_infraestrutura = models.DecimalField(
      max_digits=9,
      decimal_places=6,
      default=0.0,
   )
   valor_custo_insumo = models.DecimalField(
      max_digits=9,
      decimal_places=6,
      default=0.0,
   )

   def get_valor_custo_volume_total(self):
      return (self.valor_custo_operacional + self.valor_custo_infraestutura + self.valor_custo_insumo)

   valor_custo_volume_total = property(get_valor_custo_volume_total)

   def get_valor_custo_volume_ml(self):
      return (self.valor_custo_volume_total / self.volume_produzido)

   valor_custo_volume_ml = property(get_valor_custo_volume_ml)

   quantidade_dindin_produzido = models.PositiveIntegerField(
      default=0,
   )

   def get_valor_custo_volume_por_dindin(self):
      return (self.valor_custo_volume_total / self.quantidade_dindin_produzido)

   valor_custo_volume_por_dindin = property(get_valor_custo_volume_por_dindin)

   def get_rendimento_volume_por_dindin(self):
      return (self.volume_produzido / self.quantidade_dindin_produzido)

   rendimento_volume_por_dindin = property(get_rendimento_volume_por_dindin)

   class Meta:
      abstract = True


class LoteBase(LoteCusto):
   def __str__(self):
      return "%i - %s" % (self.id, self.data_producao)


class LoteSabor(LoteCusto):
   def __str__(self):
      return "%i - %s" % (self.id, self.data_producao)


class LoteProduto(LoteCusto):
   def __str__(self):
      return "%i - %s" % (self.id, self.data_producao)


class TipoBase(Seguranca, Restricao):
   nome = models.CharField(
      max_length=150,
   )
   descricao = models.TextField(
      max_length=512,
   )

   def get_absolute_url(self):
      return 'tipo_sabor_list'

   def save(self, *args, **kwargs):
      self.restringir()
      return super(TipoBase, self).save(*args, **kwargs)

   def delete(self, *args, **kwargs):
      self.excluir()
      super(TipoBase, self).save(*args, **kwargs)
      return

   def __str__(self):
      return self.nome


class Base(BaseCusto):
   lote = models.ForeignKey(
      LoteBase,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )
   tipo_de_base = models.ForeignKey(
      TipoBase,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )

   def __str__(self):
      return "%s %s - %i ml" % (self.tipo_de_base.nome, str(self.data_base), self.volume_estoque)


class BaseInsumo(models.Model):
   base = models.ForeignKey(
      Base,
      on_delete=models.CASCADE,
   )
   insumo = models.ForeignKey(
      Insumo,
      on_delete=models.PROTECT,
   )
   quantidade = models.PositiveSmallIntegerField()
   valor_custo_unitario = models.DecimalField(
      max_digits=9,
      decimal_places=6,
      default=0.0,
   )

   def get_valor_custo_total(self):
      return (self.quantidade * self.valor_custo_unitario)

   valor_custo_total = property(get_valor_custo_total)

   def __str__(self):
      return "%s - %i - %f" % (self.insumo.nome, self.quantidade, self.valor_custo_total)


class BaseConsumo(models.Model):
   base = models.ForeignKey(
      Base,
      on_delete=models.CASCADE,
   )
   data_consumo = models.DateTimeField(
      auto_now_add=True,
   )
   volume_consumido = models.PositiveSmallIntegerField()

   def __str__(self):
      return "%s - %i" % (str(self.data_consumo), self.volume_consumido)


class BaseDescarte(models.Model):
   base = models.ForeignKey(
      Base,
      on_delete=models.CASCADE,
   )
   data_descarte = models.DateTimeField(
      auto_now_add=True,
   )
   volume_descarte = models.PositiveSmallIntegerField()

   def __str__(self):
      return "%s - %i" % (str(self.data_descarte), self.volume_descarte)

      # class TipoInsumo(Seguranca, Restricao):
      # nome = models.CharField(
      # max_length=150,
      # )
      # descricao = models.TextField(
      # max_length=512,
      # )

      # def __str__(self):
      # return "%i - %s" % (self.id, self.nome)


class TipoSabor(Seguranca, Restricao):
   nome = models.CharField(
      max_length=150,
   )
   descricao = models.TextField(
      max_length=512,
   )

   def get_absolute_url(self):
      return 'tipo_sabor_list'

   def save(self, *args, **kwargs):
      self.restringir()
      return super(TipoSabor, self).save(*args, **kwargs)

   def delete(self, *args, **kwargs):
      self.excluir()
      super(TipoSabor, self).save(*args, **kwargs)
      return

   def __str__(self):
      return "%i - %s" % (self.id, self.nome)


class Sabor(BaseCusto):
   lote = models.ForeignKey(
      LoteSabor,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )
   tipo_sabor = models.ForeignKey(
      TipoSabor,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )

   def get_absolute_url(self):
      return 'sabor_list'

   def delete(self, *args, **kwargs):
      self.excluido_em = timezone.now()
      self.esta_ativo = False
      self.esta_excluido = True
      super(Sabor, self).save(*args, **kwargs)
      return


class SaborBase(models.Model):
   sabor = models.ForeignKey(
      Sabor,
      on_delete=models.CASCADE,
   )
   base = models.ForeignKey(
      Base,
      on_delete=models.CASCADE,
   )
   volume = models.PositiveSmallIntegerField()
   valor_custo_unitario = models.DecimalField(
      max_digits=9,
      decimal_places=6,
   )

   def get_valor_custo_total(self):
      return (self.volume * self.valor_custo_unitario)

   valor_custo_total = property(get_valor_custo_total)

   def __str__(self):
      return "%s - %i - %f" % ((self.base.data_producao), self.volume, self.valor_custo_total)


class SaborInsumo(models.Model):
   sabor = models.ForeignKey(
      Sabor,
      on_delete=models.CASCADE,
   )
   insumo = models.ForeignKey(
      Insumo,
      on_delete=models.CASCADE,
      limit_choices_to={'esta_ativo': True},
   )
   volume = models.PositiveSmallIntegerField()
   valor_custo_unitario = models.DecimalField(
      max_digits=9,
      decimal_places=6,
   )

   def get_valor_custo_total(self):
      return (self.volume * self.valor_custo_unitario)

   valor_custo_total = property(get_valor_custo_total)

   def __str__(self):
      return "%s - %i - %f" % ((self.base.data_producao), self.volume, self.valor_custo_total)


class SaborConsumo(models.Model):
   sabor = models.ForeignKey(
      Sabor,
      on_delete=models.CASCADE,
   )
   data_consumo = models.DateTimeField(
      auto_now_add=True)
   volume_consumido = models.PositiveSmallIntegerField()

   def __str__(self):
      return "%s - %i" % (str(self.data_consumo), self.volume_consumido)


class SaborDescarte(models.Model):
   sabor = models.ForeignKey(
      Sabor,
      on_delete=models.CASCADE,
   )
   data_descarte = models.DateTimeField(
      auto_now_add=True,
   )
   volume_descarte = models.PositiveSmallIntegerField()

   def __str__(self):
      return "%s - %i" % (str(self.data_descarte), self.volume_descarte)


class TipoProduto(Seguranca, Restricao):
   nome = models.CharField(
      max_length=150,
   )
   descricao = models.TextField(
      max_length=512,
   )
   quantidade_estoque_minimo = models.PositiveIntegerField(
      default=0,
   )
   quantidade_estoque_mes_anterior = models.PositiveIntegerField(
      default=0,
      editable=False,
   )
   preco_varejo_sugerido = models.DecimalField(
      max_digits=5,
      decimal_places=2,
      default=0,
   )
   preco_varejo_minimo = models.DecimalField(
      max_digits=5,
      decimal_places=2,
      default=0,
   )
   preco_atacado_sugerido = models.DecimalField(
      max_digits=5,
      decimal_places=2,
      default=0,
   )
   preco_atacado_minimo = models.DecimalField(
      max_digits=5,
      decimal_places=2,
      default=0,
   )

   @classmethod
   def sugere_valor(self, tipo):
      if tipo == VENDA_NO_VAREJO:
         return self.preco_varejo_sugerido
      if tipo == VENDA_NO_ATACADO:
         return self.preco_atacado_sugerido
      return 0.0

   @classmethod
   def valor_esta_aceitavel(self, tipo, valor):
      if tipo == VENDA_NO_VAREJO:
         return (self.preco_varejo_minimo >= valor)
      if tipo == VENDA_NO_ATACADO:
         return (self.preco_atacado_minimo >= valor)
      return False

   def get_absolute_url(self):
      return 'tipo_sabor_list'

   def save(self, *args, **kwargs):
      self.restringir()
      return super(TipoProduto, self).save(*args, **kwargs)

   def delete(self, *args, **kwargs):
      self.excluir()
      super(TipoProduto, self).save(*args, **kwargs)
      return

   def __str__(self):
      return "%i - %s" % (self.id, self.nome)


class Produto(Seguranca, Restricao):
   lote = models.ForeignKey(
      LoteProduto,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )
   data_producao = models.DateTimeField(
      auto_now_add=True,
   )
   tipo_produto = models.ForeignKey(
      TipoProduto,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )
   quantidade_produzido = models.PositiveIntegerField()
   quantidade_vendido = models.PositiveIntegerField(default=0)
   quantidade_descartado = models.PositiveIntegerField(
      default=0,
   )

   def get_quantidade_estoque(self):
      return (self.quantidade_produzido - (self.quantidade_vendido + self.quantidade_descartado))

   quantidade_estoque = property(get_quantidade_estoque)

   valor_custo_insumo = models.DecimalField(
      max_digits=9,
      decimal_places=6,
      default=0,
   )
   valor_custo_operacional = models.DecimalField(
      max_digits=9,
      decimal_places=6,
      default=0,
   )
   valor_custo_infraestrutura = models.DecimalField(
      max_digits=9,
      decimal_places=6,
      default=0,
   )

   def get_valor_custo_produto_total(self):
      return (self.valor_custo_insumo + self.valor_custo_operacional + self.valor_custo_infraestrutura)

   valor_custo_produto_total = property(get_valor_custo_produto_total)

   def get_valor_custo_produto_unitario(self):
      return (self.valor_custo_produto_unitario / self.quantidade_produzido)

   valor_custo_produto_unitario = property(get_valor_custo_produto_unitario)

   def __str__(self):
      return self.nome


class ProdutoSabor(models.Model):
   produto = models.ForeignKey(
      Produto,
      on_delete=models.CASCADE,
   )
   sabor = models.ForeignKey(
      Sabor,
      on_delete=models.PROTECT,
   )


class ProdutoInsumo(models.Model):
   produto = models.ForeignKey(
      Produto,
      on_delete=models.CASCADE,
   )
   insumo = models.ForeignKey(
      Insumo,
      on_delete=models.PROTECT,
   )
   quantidade = models.PositiveSmallIntegerField()
   valor_custo_unitario = models.DecimalField(
      max_digits=12,
      decimal_places=6,
   )

   def get_valor_custo_total(self):
      return (self.quantidade * self.valor_custo_unitario)

   valor_custo_total = property(get_valor_custo_total)


class ProdutoBase(models.Model):
   produto = models.ForeignKey(
      Produto,
      on_delete=models.PROTECT,
   )
   base = models.ForeignKey(
      Base,
      on_delete=models.PROTECT,
   )
   quantidade = models.PositiveSmallIntegerField()
   valor_custo_unitario = models.DecimalField(
      max_digits=12,
      decimal_places=6,
   )

   def get_valor_custo_total(self):
      return (self.quantidade * self.valor_custo_unitario)

   valor_custo_total = property(get_valor_custo_total)


class ReposicaoInsumo(models.Model):
   data_reposicao = models.DateTimeField()
   item = models.ForeignKey(
      Item,
      on_delete=models.PROTECT,
      limit_choices_to={'esta_ativo': True},
   )
   quantidade = models.PositiveIntegerField()

   def get_volume(self):
      return (self.item.volume_unitario * self.quantidade)

   volume = property(get_volume)

   def get_valor_custo_ml(self):
      return (self.item.valor_custo_ultima_compra / self.item.volume_unitario)

   valor_custo_medida = property(get_valor_custo_ml)

   def get_valor_custo_medio_ml(self):
      return (self.item.valor_custo_medio / self.item.volume_unitario)

   valor_custo_medio_medida = property(get_valor_custo_medio_ml)

   def __str__(self):
      return "%s - %i - %f" % (self.item.nome, self.quantidade, self_valor_custo_medio)
