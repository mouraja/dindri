from django.db import models
from django.utils import timezone
from utils.models import Seguranca, Endereco

# Create your models here.

SEXO_MASCULINO = 'M'
SEXO_FEMININO = 'F'

SEXO_CHOICES = (
   (SEXO_FEMININO, 'Feminino'),
   (SEXO_MASCULINO, 'Masculino'),
)


class Cliente(Seguranca, Endereco):
   '''Clientes da DinDri Deliciosos'''
   nome = models.CharField(
      max_length=150,
   )
   nome_preferencial = models.CharField(
      max_length=50,
   )
   sexo = models.CharField(
      max_length=1,
      choices=SEXO_CHOICES,
      null=True,
      blank=True,
   )
   endereco = models.TextField(
      max_length=512,
      null=True,
      blank=True,
   )
   watsapp = models.CharField(
      max_length=15,
      null=True,
      blank=True,
   )
   celular = models.CharField(
      max_length=15,
      null=True,
      blank=True,
   )
   fone_residencial = models.CharField(
      max_length=15,
      null=True,
      blank=True,
   )
   interfone = models.CharField(
      max_length=12,
      null=True,
      blank=True,
   )
   email = models.EmailField(
      max_length=256,
      null=True,
      blank=True,
   )
   observacao = models.TextField(
      max_length=512,
      null=True,
      blank=True,
   )
   data_aniversario = models.DateField(
      null=True,
      blank=True,
   )
   responsavel = models.ForeignKey(
      'self',
      on_delete=models.SET_NULL,
      limit_choices_to={'esta_ativo': True},
      null=True,
      blank=True,
   )
   esta_bloqueado = models.BooleanField(
      default=False,
   )
   motivo_bloqueio = models.TextField(
      max_length=1024,
      null=True,
      blank=True,
   )
   bloqueado_em = models.DateTimeField(null=True, blank=True)

   @classmethod
   def is_bloqueado(self):
      return self.esta_bloqueado

   def get_absolute_url(self):
      return 'cliente_list'

   def delete(self, *args, **kwargs):
      self.excluir()
      super(Cliente, self).save(*args, **kwargs)
      return

   def __str__(self):
      return "%i - %s" % (self.id, self.nome_preferencial)
