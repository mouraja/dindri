from django.db import models
from django.utils import timezone

# Create your models here.

UF_AC = 'AC'
UF_AL = 'AL'
UF_AP = 'AP'
UF_AM = 'AM'
UF_BA = 'BA'
UF_CE = 'CE'
UF_DF = 'DF'
UF_GO = 'GO'
UF_MT = 'MT'
UF_MS = 'MS'
UF_MA = 'MA'
UF_MG = 'MG'
UF_PA = 'PA'
UF_PB = 'PB'
UF_PR = 'PR'
UF_PE = 'PE'
UF_PI = 'PI'
UF_RN = 'RN'
UF_RS = 'RS'
UF_RO = 'RO'
UF_RR = 'RR'
UF_SC = 'SC'
UF_SP = 'SP'
UF_SE = 'SE'
UF_TO = 'TO'

UFS_CHOICES = (
   (UF_AC, 'Acre'),
   (UF_AL, 'Alagoas'),
   (UF_AP, 'Amapá'),
   (UF_AM, 'Amazonas'),
   (UF_BA, 'Bahia'),
   (UF_CE, 'Ceará'),
   (UF_DF, 'Distrito Federal'),
   (UF_GO, 'Goiás'),
   (UF_MT, 'Mato Grosso'),
   (UF_MS, 'Mato Grosso Sul'),
   (UF_MA, 'Maranhão'),
   (UF_MG, 'Minas Gerais'),
   (UF_PA, 'Pará'),
   (UF_PB, 'Paraíba'),
   (UF_PR, 'Paraná'),
   (UF_PE, 'Pernambuco'),
   (UF_PI, 'Piauí'),
   (UF_RN, 'Rio Grande do Norte'),
   (UF_RS, 'Rio Grande do Sul'),
   (UF_RO, 'Rondônia'),
   (UF_RR, 'Roraima'),
   (UF_SC, 'Santa Catarina'),
   (UF_SP, 'São Paulo'),
   (UF_SE, 'Sergipe'),
   (UF_TO, 'Tocantins'),
)


class Seguranca(models.Model):
   esta_ativo = models.BooleanField(default=True)
   esta_excluido = models.BooleanField(default=False)
   criado_em = models.DateTimeField(auto_now_add=True)
   alterado_em = models.DateTimeField(auto_now=True)
   excluido_em = models.DateTimeField(null=True, blank=True)
   ativado_em = models.DateTimeField(null=True, blank=True)
   desativado_em = models.DateTimeField(null=True, blank=True)

   class Meta:
      abstract = True

   @classmethod
   def is_ativo(self):
      return self.esta_ativo

   def desativar(self):
      self.esta_ativo = False
      self.desativado_em = timezone.now()

   def ativar(self):
      self.esta_ativo = True
      self.ativado_em = timezone.now()

   def excluir(self):
      self.esta_ativo = False
      self.esta_excluido = True
      self.excluido_em = timezone.now()


class Restricao(models.Model):
   tem_restricao = models.BooleanField(default=False)
   restricoes = models.TextField(max_length=500, null=True, blank=True)

   class Meta:
      abstract = True

   def restringir(self):
      self.tem_restricao = (
         self.restricoes is not None
         and self.restricoes.strip() != '')

   @classmethod
   def is_restrito(self):
      return self.tem_restricao


class Endereco(models.Model):
   logradouro = models.CharField(
      max_length=256,
      null=True,
      blank=True)
   complemento = models.CharField(
      max_length=256,
      null=True,
      blank=True)
   bairro = models.CharField(
      max_length=128,
      null=True,
      blank=True)
   cidade = models.CharField(
      max_length=128,
      null=True,
      blank=True)
   uf = models.CharField(
      max_length=2,
      choices=UFS_CHOICES,
      null=True,
      blank=True,
      default=UF_DF)
   cep = models.CharField(
      max_length=10,
      null=True,
      blank=True)

   class Meta:
      abstract = True
