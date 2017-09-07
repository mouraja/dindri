from django import forms
from django.forms.models import inlineformset_factory
from producao.models import Insumo, TipoBase, TipoSabor, TipoProduto, \
   Produto, ProdutoSabor, ProdutoInsumo, \
   Base, BaseInsumo, BaseConsumo, BaseDescarte, \
   Sabor, SaborBase, SaborInsumo, SaborConsumo, SaborDescarte, \
   LoteBase, LoteSabor, LoteProduto


class InsumoForm(forms.ModelForm):
   class Meta:
      model = Insumo
      fields = '__all__'


class LoteBaseForm(forms.ModelForm):
   class Meta:
      model = LoteBase
      fields = '__all__'


class LoteSaborForm(forms.ModelForm):
   class Meta:
      model = LoteSabor
      fields = '__all__'


class LoteProdutoForm(forms.ModelForm):
   class Meta:
      model = LoteProduto
      fields = '__all__'


### TipoSabor
class TipoSaborForm(forms.ModelForm):
   class Meta:
      model = TipoSabor
      fields = '__all__'


class TipoSaborDeleteForm(forms.ModelForm):
   class Meta:
      model = TipoSabor
      fields = (
         'nome',
         'descricao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'readonly': 'readonly', 'size': '80px', 'class': 'control-form'}),
         'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'control-form'}),
      }


class TipoSaborActiveForm(forms.ModelForm):
   class Meta:
      model = TipoSabor
      fields = (
         'nome',
         'descricao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'readonly': 'readonly', 'size': '80px', 'class': 'control-form'}),
         'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'control-form'}),
      }

   def save(self, commit=True):
      instance = super(TipoSaborActiveForm, self).save(commit=False)
      if instance.is_ativo:
         instance.desativar()
      else:
         instance.ativar()
      if commit:
         instance.save()
      return instance


class TipoSaborCreateUpdateForm(forms.ModelForm):
   class Meta:
      model = TipoSabor
      fields = (
         'nome',
         'descricao',
         'restricoes',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'maxlenght': '150', 'size': '80px', 'class': 'control-form'}),
         'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'control-form'}),
         'restricoes': forms.Textarea(attrs={'cols': 80, 'rows': 6, 'class': 'control-form'}),
      }


class TipoSaborDetailForm(forms.ModelForm):
   class Meta:
      model = TipoSabor
      fields = (
         'nome',
         'descricao',
         'tem_restricao',
         'restricoes',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'readonly': 'readonly', 'size': '80px', 'class': 'control-form'}),
         'descricao': forms.Textarea(attrs={'readonly': 'readonly', 'cols': 80, 'rows': 3, 'class': 'control-form'}),
         'restricoes': forms.Textarea(attrs={'readonly': 'readonly', 'cols': 80, 'rows': 6, 'class': 'control-form'}),
      }


### TipoBase
class TipoBaseForm(forms.ModelForm):
   class Meta:
      model = TipoBase
      fields = '__all__'


class TipoBaseDeleteForm(forms.ModelForm):
   class Meta:
      model = TipoBase
      fields = (
         'nome',
         'descricao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'readonly': 'readonly', 'size': '80px', 'class': 'control-form'}),
         'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'control-form'}),
      }


class TipoBaseActiveForm(forms.ModelForm):
   class Meta:
      model = TipoBase
      fields = (
         'nome',
         'descricao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'readonly': 'readonly', 'size': '80px', 'class': 'control-form'}),
         'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'control-form'}),
      }

   def save(self, commit=True):
      instance = super(TipoBaseActiveForm, self).save(commit=False)
      if instance.is_ativo:
         instance.desativar()
      else:
         instance.ativar()
      if commit:
         instance.save()
      return instance


class TipoBaseCreateUpdateForm(forms.ModelForm):
   class Meta:
      model = TipoBase
      fields = (
         'nome',
         'descricao',
         'restricoes',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'maxlenght': '150', 'size': '80px', 'class': 'control-form'}),
         'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'control-form'}),
         'restricoes': forms.Textarea(attrs={'cols': 80, 'rows': 6, 'class': 'control-form'}),
      }


class TipoBaseDetailForm(forms.ModelForm):
   class Meta:
      model = TipoBase
      fields = (
         'nome',
         'descricao',
         'tem_restricao',
         'restricoes',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'readonly': 'readonly', 'size': '80px', 'class': 'control-form'}),
         'descricao': forms.Textarea(attrs={'readonly': 'readonly', 'cols': 80, 'rows': 3, 'class': 'control-form'}),
         'restricoes': forms.Textarea(attrs={'readonly': 'readonly', 'cols': 80, 'rows': 6, 'class': 'control-form'}),
      }


# TipoProduto
class TipoProdutoForm(forms.ModelForm):
   class Meta:
      model = TipoProduto
      fields = '__all__'


class TipoProdutoDeleteForm(forms.ModelForm):
   class Meta:
      model = TipoProduto
      fields = (
         'nome',
         'descricao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'readonly': 'readonly', 'size': '80px', 'class': 'control-form'}),
         'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'control-form'}),
      }


class TipoProdutoDetailForm(forms.ModelForm):
   class Meta:
      model = TipoProduto
      fields = (
         'nome',
         'descricao',
         'tem_restricao',
         'restricoes',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'readonly': 'readonly', 'size': '80px', 'class': 'control-form'}),
         'descricao': forms.Textarea(attrs={'readonly': 'readonly', 'cols': 80, 'rows': 3, 'class': 'control-form'}),
         'restricoes': forms.Textarea(attrs={'readonly': 'readonly', 'cols': 80, 'rows': 6, 'class': 'control-form'}),
      }


class TipoProdutoActiveForm(forms.ModelForm):
   class Meta:
      model = TipoProduto
      fields = (
         'esta_ativo',
         'nome',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'readonly': 'readonly', 'size': '80px', 'class': 'control-form'}),
         'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 6, 'class': 'control-form'}),
      }

   def save(self, commit=True):
      instance = super(TipoProdutoActiveForm, self).save(commit=False)
      if instance.is_ativo:
         instance.desativar()
      else:
         instance.ativar()
      if commit:
         instance.save()
      return instance


class TipoProdutoCreateUpdateForm(forms.ModelForm):
   class Meta:
      model = TipoProduto
      fields = (
         'nome',
         'descricao',
         'restricoes',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'maxlength': '150', 'size': '80px', 'class': 'control-form'}),
         'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'class': 'control-form'}),
         'restricoes': forms.Textarea(attrs={'cols': 80, 'rows': 6, 'class': 'control-form'}),
      }


class BaseForm(forms.ModelForm):
   class Meta:
      model = Base
      fields = '__all__'


class SaborForm(forms.ModelForm):
   class Meta:
      model = Sabor
      fields = '__all__'


class ProdutoForm(forms.ModelForm):
   class Meta:
      model = Produto
      fields = '__all__'


class ProdutoCreateForm(forms.ModelForm):
   class Meta:
      model = Produto
      fields = (
         'lote',
         'tipo_produto',
         'quantidade_produzido',
      )


class ProdutoAdcionaForm(forms.ModelForm):
   class Meta:
      model = Produto
      fields = '__all__'


BaseInsumoFormSet = inlineformset_factory(Base, BaseInsumo, form=BaseForm)
SaborInsumoFormSet = inlineformset_factory(Sabor, SaborInsumo, form=SaborForm)
SaborBaseFormSet = inlineformset_factory(Sabor, SaborBase, form=SaborForm)
ProdutoSaborFormSet = inlineformset_factory(Produto, ProdutoSabor, form=ProdutoForm)
ProdutoInsumoFormSet = inlineformset_factory(Produto, ProdutoInsumo, form=ProdutoForm)
