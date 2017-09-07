from django.db import models
from producao.models import TipoProduto
from estoque.models import Categoria
from utils.models import Seguranca

# Create your models here.

MILILITRO = 'ml'
GRAMA = 'g'
UNIDADE = 'un'

UNIDADE_MEDIDA = (
   (MILILITRO, 'Mililitro'),
   (GRAMA, 'Grama'),
   (UNIDADE, 'Unidade'),
)


class Receita(Seguranca):
   nome = models.CharField(
      max_length=150,
   )
   produto = models.ForeignKey(
      TipoProduto,
      on_delete=models.SET_NULL,
      limit_choices_to={'esta_ativo': True},
      null=True,
      blank=True,
   )
   descricao = models.CharField(
      max_length=512,
   )

   def __str__(self):
      return "%i - %s" % (self.id, self.nome)


class ReceitaIngrediente(models.Model):
   receita = models.ForeignKey(
      Receita,
      on_delete=models.CASCADE,
      limit_choices_to={'esta_ativo': True},
   )
   ingrediente = models.ForeignKey(
      Categoria,
      on_delete=models.SET_NULL,
      null=True,
      blank=True,
   )
   volume = models.PositiveIntegerField(
      default=0,
   )
   unidade = models.CharField(
      max_length=2,
      choices=UNIDADE_MEDIDA,
      default=MILILITRO,
   )

   def __str__(self):
      return "%s - %i %s" % (self.ingrediente.nome, self.volume, self.unidade)


class ReceitaInstrucao(models.Model):
   receita = models.ForeignKey(
      Receita,
      on_delete=models.CASCADE,
      limit_choices_to={'esta_ativo': True},
   )
   passo = models.PositiveSmallIntegerField()
   instrucao = models.TextField(max_length=1024)

   def __str__(self):
      return "%s - %i %s" % (self.ingrediente.nome, self.volume, self.unidade)
