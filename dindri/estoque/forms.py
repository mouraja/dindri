from django import forms
from estoque.models import Categoria, Item, Entrada, Saida


class CategoriaForm(forms.ModelForm):
   class Meta:
      model = Categoria
      fields = '__all__'


class CategoriaCreateUpdateForm(forms.ModelForm):
   class Meta:
      model = Categoria
      fields = (
         'nome',
         'descricao',
         'restricoes',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'size': '80px', 'maxlength': '150', 'class': 'control-form'}, ),
         'descricao': forms.Textarea(attrs={'cols': '80', 'rows': '6', 'class': 'control-form'}, ),
         'restricoes': forms.Textarea(attrs={'cols': '80', 'rows': '6', 'class': 'control-form'}, ),
      }


class CategoriaDeleteForm(forms.ModelForm):
   class Meta:
      model = Categoria
      fields = (
         'nome',
         'descricao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'class': 'control-form', 'readonly': 'readonly'}, ),
         'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 6, 'class': 'control-form', 'readonly': 'readonly'}, ),
      }


class CategoriaActiveForm(forms.ModelForm):
   class Meta:
      model = Categoria
      fields = (
         'esta_ativo',
         'nome',
         'descricao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'size': '80px', 'class': 'control-form', 'readonly': 'readonly'}, ),
         'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 6, 'class': 'control-form'}, ),
      }

   def save(self, commit=True):
      instance = super(CategoriaActiveForm, self).save(commit=False)
      print(instance.esta_ativo)
      if instance.esta_ativo:
         instance.desativar()
      else:
         instance.ativar()
      if commit:
         instance.save()
      return instance


class CategoriaDetailForm(forms.ModelForm):
   class Meta:
      model = Categoria
      fields = (
         'nome',
         'descricao',
         'restricoes',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'class': 'control-form', 'readonly': 'readonly'}, ),
         'descricao': forms.Textarea(
            attrs={'cols': '80', 'rows': '6', 'class': 'control-form', 'readonly': 'readonly'}, ),
         'restricoes': forms.Textarea(
            attrs={'cols': '80', 'rows': '6', 'class': 'control-form', 'readonly': 'readonly'}, ),
      }


###   Item
class ItemForm(forms.ModelForm):
   class Meta:
      model = Item
      fields = '__all__'


class ItemCreateUpdateForm(forms.ModelForm):
   class Meta:
      model = Item
      fields = (
         'categoria',
         'nome',
         'descricao',
         'volume_unitario',
         'unidade',
         'quantidade',
         'restricoes',
      )
      widgets = {
         'nome': forms.TextInput(attrs={
            'class': 'control-form, form-field-black',
            'size': '80px',
            'maxlength': '150'
         }),
         'descricao': forms.Textarea(attrs={
            'cols': '80',
            'rows': '3',
            'class': 'control-form, form-field-black',
         }),
         'volume_unitario': forms.NumberInput(attrs={
            'step': '1',
            'class': 'control-form, form-field-black',
         }),
         'unidade': forms.Select(attrs={
            'class': 'control-form, form-field-black',
         }),
         'quantidade': forms.NumberInput(attrs={
            'step': '1',
            'class': 'control-form, form-field-black',
         }),
         'restricoes': forms.Textarea(attrs={
            'cols': '80',
            'rows': '3',
            'class': 'control-form, form-field-black',
         }),
      }


class ItemDetailForm(forms.ModelForm):
   class Meta:
      model = Item
      fields = (
         'categoria',
         'nome',
         'descricao',
         'volume_unitario',
         'unidade',
         'quantidade',
         'restricoes',
      )


class ItemActiveForm(forms.ModelForm):
   class Meta:
      model = Item
      fields = (
         'nome',
         'descricao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'class': 'control-form', 'size': '80px', 'maxlength': '150'}, ),
         'descricao': forms.Textarea(attrs={'cols': '80', 'rows': '3'}, ),
      }

   def save(self, commit=True):
      instance = super(ItemActiveForm, self).save(commit=False)
      if instance.is_ativo:
         instance.desativar()
      else:
         instance.ativar()
      if commit:
         instance.save()
      return instance


class ItemDeleteForm(forms.ModelForm):
   class Meta:
      model = Item
      fields = (
         'nome',
         'descricao',
      )
      widgets = {
         'nome': forms.TextInput(attrs={'class': 'control-form', 'size': '80px', 'maxlength': '150'}, ),
         'descricao': forms.Textarea(attrs={'cols': '80', 'rows': '3'}, ),
      }


###   Entrada
class EntradaForm(forms.ModelForm):
   class Meta:
      model = Entrada
      fields = '__all__'


class SaidaForm(forms.ModelForm):
   class Meta:
      model = Saida
      fields = '__all__'
