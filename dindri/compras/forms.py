from django import forms
from django.utils import timezone
from django.forms.models import inlineformset_factory
from compras.models import Pedido, Compra, PedidoItem, CompraItem, Fornecedor
from compras.models import COMPRA_FECHADA, COMPRA_CANCELADA, COMPRA_ABERTA, COMPRA_PENDENTE
from compras.models import ITEM_ATENDIDO, ITEM_PENDENTE, ITEM_CANCELADO

class PedidoForm(forms.ModelForm):
   class Meta:
      model = Pedido
      fields = '__all__'

##  Pedido
class PedidoCreateForm(forms.ModelForm):
   class Meta:
      model = Pedido
      fields = (
         'data_limite',
         'solicitante',
         'observacao',
      )
      widgets = {
         'data_limite': forms.DateTimeInput(attrs={
            'type': 'date',
            'class': 'control-form, field-form-black',
         }),
         'solicitante': forms.TextInput(attrs={
            'size': '80px',
            'maxlength': '256',
            'class': 'control-form, field-form-black',
         }),
         'observacao': forms.Textarea(attrs={
            'cols': '80',
            'rows': '6',
            'class': 'control-form, field-form-black',
         }),
      }

class PedidoUpdateForm(forms.ModelForm):
   class Meta:
      model = Pedido
      fields = (
         'data_limite',
         'solicitante',
         'observacao',
         'situacao_pedido',
      )
      widgets = {
         'data_limite': forms.DateTimeInput(attrs={
            'type': 'date',
            'class': 'control-form, field-form-black',
         }),
         'solicitante': forms.TextInput(attrs={
            'size': '80px',
            'maxlength': '256',
            'class': 'control-form, field-form-black',
         }),
         'observacao': forms.Textarea(attrs={
            'cols': '80',
            'rows': '6',
            'class': 'control-form, field-form-black',
         }),
         'situacao_pedido': forms.Select(attrs={
            'class': 'control-form, field-form-black',
         }),
      }

##  PeditoItem
class PedidoItemCreateForm(forms.ModelForm):
   class Meta:
      model = PedidoItem
      fields = (
         'item',
         'quantidade',
         'descricao',
      )
      widgets = {
         'item': forms.Select(attrs={
            'class': 'control-form, field-form-black',
         }),
         'quantidade': forms.NumberInput(attrs={
            'min': '1',
            'step': '5',
            'class': 'control-form, field-form-black',
         }),
         'descricao': forms.Textarea(attrs={
            'cols': '50',
            'rows': '3',
            'class': 'control-form, field-form-black',
         }),
      }

class PedidoItemUpdateForm(forms.ModelForm):
   class Meta:
      model = PedidoItem
      fields = (
         'situacao_item',
         'item',
         'quantidade',
         'descricao',
      )
      widgets = {
         'situacao_item': forms.Select(attrs={
            'class': 'control-form, field-form-black',
         }),
         'item': forms.Select(attrs={
            'class': 'control-form, field-form-black',
            'readonly': 'readonly',
         }),
         'quantidade': forms.NumberInput(attrs={
            'min': '1',
            'step': '5',
            'class': 'control-form, field-form-black',
         }),
         'descricao': forms.Textarea(attrs={
            'cols': '50',
            'rows': '3',
            'class': 'control-form, field-form-black',
         }),
      }

##  Compra
class CompraForm(forms.ModelForm):
   class Meta:
      model = Compra
      fields = '__all__'
      widgets = {
         'data_compra': forms.DateTimeInput(attrs={
            'type': 'date',
            'class': 'control-form'}),
         'valor_total': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form'}),
      }

class CompraCreateForm(forms.ModelForm):
   #'pedido',
   class Meta:
      model = Compra
      fields = (
         'fornecedor',
         'nota_fiscal',
         'data_compra',
         'valor_total',
         'situacao_compra',
      )
      widgets = {
         'fornecedor': forms.Select(attrs={
            'width': '50px',
            'class': 'control-form, field-form-black',
            'required': 'required',
         }),
         'nota_fiscal': forms.TextInput(attrs={
            'size': '50px',
            'maxlength': '64',
            'class': 'control-form, field-form-black',
         }),
         '''
         'pedido': forms.SelectMultiple(attrs={
            'width': '50px',
            'size': '5',
            'class': 'control-form, field-form-black',
         }),
         '''
         'data_compra': forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'control-form, field-form-black',
         }),
         'valor_total': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'situacao_compra': forms.HiddenInput(attrs={
            'value': COMPRA_PENDENTE,
         })
      }

class CompraUpdateForm(forms.ModelForm):
   class Meta:
      model = Compra
      fields = (
         'fornecedor',
         'nota_fiscal',
         'data_compra',
         'valor_total',
         'situacao_compra',
      )
      readonly_fields = (
         'data_emissao',
      )
      widgets = {
         'fornecedor': forms.Select(attrs={
            'class': 'control-form, field-form-black',
            'required': 'required',
         }),
         'nota_fiscal': forms.TextInput(attrs={
            'size': '50px',
            'maxlength': '64',
            'class': 'control-form, field-form-black',
         }),
         'data_compra': forms.DateTimeInput(attrs={
            'type': 'datetime',
            'class': 'control-form',
         }),
         'valor_total': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form',
         }),
         'situacao_compra': forms.HiddenInput(attrs={
            'value': COMPRA_ABERTA,
         })
      }

class CompraDoneForm(forms.ModelForm):

   class Meta:
      model = Compra
      fields = '__all__'
      '''
      fields = (
         'fornecedor',
         'nota_fiscal',
         'data_compra',
         'valor_total',
         'situacao_compra',
      )
      widgets = {
         'fornecedor': forms.Select(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'nota_fiscal': forms.TextInput(attrs={
            'size': '50px',
            'maxlength': '64',
            'class': 'control-form, field-form-black',
         }),
         'data_compra': forms.DateTimeInput(attrs={
            'required': 'required',
            'class': 'control-form, field-form-black',
         }),
         'valor_total': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'situacao_compra': forms.HiddenInput(attrs={
            'value': COMPRA_FECHADA,
         })
      }
      '''

   def save(self, commit=True):
      print("estou no save CompraDoneForm")
      instance = super(CompraDoneForm, self).save(commit=False)
      print("esta ativo %b" % (self.esta_ativo))
      instance.concluir()
      if commit:
         instance.save()
      return instance

class CompraCancelForm(forms.ModelForm):
   class Meta:
      model = Compra
      fields = (
         'fornecedor',
         'nota_fiscal',
         'data_compra',
         'valor_total',
         'situacao_compra',
      )
      widgets = {
         'fornecedor': forms.Select(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'nota_fiscal': forms.TextInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'data_compra': forms.DateTimeInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'valor_total': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'situacao_compra': forms.HiddenInput(attrs={
            'value': COMPRA_CANCELADA,
         })
      }

##  CompraItem
class CompraItemCreateForm(forms.ModelForm):
   class Meta:
      model = CompraItem
      fields = (
         'item',
         'quantidade',
         'valor_unitario',
         'valor_total',
         'situacao_item',
      )
      widgets = {
         'item': forms.Select(attrs={
            'class': 'control-form, field-form-black',
         }),
         'quantidade': forms.NumberInput(attrs={
            'onchange': 'calculate(this)',
            'class': 'control-form, field-form-black',
         }),
         'valor_unitario': forms.NumberInput(attrs={
            'onchange': 'calculate(this)',
            'class': 'control-form, field-form-black',
         }),
         'valor_total': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'situacao_item': forms.HiddenInput(attrs={
            'value': ITEM_PENDENTE,
         })
      }

class CompraItemUpdateForm(forms.ModelForm):
   class Meta:
      model = CompraItem
      fields = (
         'situacao_item',
         'item',
         'quantidade',
         'valor_unitario',
         'valor_total',
      )
      widgets = {
         'situacao_item': forms.Select(attrs={
            'class': 'contro-form, field-form-black',
         }),
         'item': forms.Select(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'quantidade': forms.NumberInput(attrs={
            'onchange': 'calculate(this)',
            'class': 'control-form, field-form-black',
         }),
         'valor_unitario': forms.NumberInput(attrs={
            'onchange': 'calculate(this)',
            'class': 'control-form, field-form-black',
         }),
         'valor_total': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
      }

class CompraItemDoneForm(forms.ModelForm):
   class Meta:
      model = CompraItem
      fields = (
         'item',
         'quantidade',
         'valor_unitario',
         'valor_total',
         'situacao_item',
      )
      widgets = {
         'item': forms.Select(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'quantidade': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'valor_unitario': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'valor_total': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'situacao_item': forms.HiddenInput(),
      }

class CompraItemCancelForm(forms.ModelForm):
   class Meta:
      model = CompraItem
      fields = (
         'situacao_item',
         'item',
         'quantidade',
         'valor_unitario',
         'valor_total',
      )
      widgets = {
         'situacao_item': forms.HiddenInput(attrs={
            'value': ITEM_CANCELADO,
         }),
         'item': forms.Select(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'quantidade': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'valor_unitario': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
         'valor_total': forms.NumberInput(attrs={
            'readonly': 'readonly',
            'class': 'control-form, field-form-black',
         }),
      }

##  Fornecedor
class FornecedorForm(forms.ModelForm):
   class Meta:
      model = Fornecedor
      fields = '__all__'

class FornecedorCreateUpdateForm(forms.ModelForm):
   class Meta:
      model = Fornecedor
      fields = (
         'tipo_fornecedor',
         'nome',
         'nome_fantasia',
         'cnpj',
         'logradouro',
         'complemento',
         'bairro',
         'cidade',
         'uf',
         'cep',
         'telefone',
         'contato',
         'email',
         'observacao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'size': '80px', 'max_length': '150', 'class': 'control-form'}),
         'nome_fantasia': forms.TextInput(attrs={'size': '80px', 'class': 'control-form'}),
         'cnpj': forms.TextInput(attrs={'size': '40px', 'class': 'control-form'}),
         'logradouro': forms.TextInput(attrs={'size': '80px', 'class': 'control-form'}),
         'complemento': forms.TextInput(attrs={'size': '80px', 'class': 'control-form'}),
         'bairro': forms.TextInput(attrs={'size': '80px', 'class': 'control-form'}),
         'cidade': forms.TextInput(attrs={'size': '80px', 'class': 'control-form'}),
         'cep': forms.TextInput(attrs={'size': '40px', 'class': 'control-form'}),
         'telefone': forms.TextInput(attrs={'size': '40px', 'class': 'control-form'}),
         'contato': forms.TextInput(attrs={'size': '80px', 'class': 'control-form'}),
         'email': forms.TextInput(attrs={'type': 'mail', 'size': '80px', 'class': 'control-form'}),
         'observacao': forms.Textarea(attrs={'cols': '80', 'rows': '3', 'class': 'control-form'}),
      }

class FornecedorActiveForm(forms.ModelForm):
   class Meta:
      model = Fornecedor
      fields = (
         'nome',
         'observacao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'size': '80px', 'readonly': 'readonly', 'class': 'control-form'}),
         'observacao': forms.Textarea(attrs={'cols': '80', 'rows': '3', 'class': 'control-form'}),
      }

   def save(self, commit=True):
      instance = super(FornecedorActiveForm, self).save(commit=False)
      instance.esta_ativo = not instance.esta_ativo
      if instance.esta_ativo:
         instance.ativado_em = timezone.now()
      else:
         instance.desativado_em = timezone.now()
      if commit:
         instance.save()
      return instance

class FornecedorDeleteForm(forms.ModelForm):
   class Meta:
      model = Fornecedor
      fields = (
         'nome',
         'observacao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={
            'size': '80px',
            'readonly': 'readonly',
            'class': 'control-form'}),
         'observacao': forms.Textarea(attrs={
            'cols': '80',
            'rows': '3',
            'class': 'control-form'}),
      }

class FornecedorDetailForm(forms.ModelForm):
   class Meta:
      model = Fornecedor
      fields = (
         'tipo_fornecedor',
         'nome',
         'nome_fantasia',
         'cnpj',
         'logradouro',
         'complemento',
         'bairro',
         'cidade',
         'uf',
         'cep',
         'telefone',
         'contato',
         'email',
         'observacao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={
            'readonly': 'readonly',
            'size': '80px',
            'max_length': '150',
            'class': 'control-form'}),
         'nome_fantasia': forms.TextInput(attrs={
            'readonly': 'readonly',
            'size': '80px',
            'class': 'control-form'}),
         'cnpj': forms.TextInput(attrs={
            'readonly': 'readonly',
            'size': '40px',
            'class': 'control-form'}),
         'logradouro': forms.TextInput(attrs={
            'readonly': 'readonly',
            'size': '80px',
            'class': 'control-form'}),
         'complemento': forms.TextInput(attrs={
            'readonly': 'readonly',
            'size': '80px',
            'class': 'control-form'}),
         'bairro': forms.TextInput(attrs={
            'readonly': 'readonly',
            'size': '80px',
            'class': 'control-form'}),
         'cidade': forms.TextInput(attrs={
            'readonly': 'readonly',
            'size': '80px',
            'class': 'control-form'}),
         'cep': forms.TextInput(attrs={
            'readonly': 'readonly',
            'size': '40px',
            'class': 'control-form'}),
         'telefone': forms.TextInput(attrs={
            'readonly': 'readonly',
            'size': '40px',
            'class': 'control-form'}),
         'contato': forms.TextInput(attrs={
            'readonly': 'readonly',
            'size': '80px',
            'class': 'control-form'}),
         'email': forms.TextInput(attrs={
            'readonly': 'readonly',
            'type': 'mail',
            'size': '80px',
            'class': 'control-form'}),
         'observacao': forms.Textarea(attrs={
            'readonly': 'readonly',
            'cols': '80',
            'rows': '3',
            'class': 'control-form'}),
      }

## Pedito FormSet
PedidoItemCreateFormSet = inlineformset_factory(
   Pedido,
   PedidoItem,
   form=PedidoItemCreateForm)

PedidoItemUpdateFormSet = inlineformset_factory(
   Pedido,
   PedidoItem,
   form=PedidoItemUpdateForm)

## Compra FormSet
CompraItemCreateFormSet = inlineformset_factory(
   Compra,
   CompraItem,
   form=CompraItemCreateForm)

CompraItemUpdateFormSet = inlineformset_factory(
   Compra,
   CompraItem,
   form=CompraItemUpdateForm,
   max_num=None,
   extra=0)

CompraItemDoneFormSet = inlineformset_factory(
   Compra,
   CompraItem,
   form=CompraItemDoneForm,
   max_num=None,
   extra=0)

CompraItemCancelFormSet = inlineformset_factory(
   Compra,
   CompraItem,
   form=CompraItemCancelForm,
   max_num=None,
   extra=0)