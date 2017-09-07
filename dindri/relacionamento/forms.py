from django import forms
from django.utils import timezone
from relacionamento.models import Cliente, SEXO_CHOICES


class ClienteForm(forms.ModelForm):
   class Meta:
      model = Cliente
      fields = '__all__'


class ClienteCreateUpdateForm(forms.ModelForm):
   class Meta:
      model = Cliente
      fields = (
         'nome',
         'nome_preferencial',
         'endereco',
         'watsapp',
         'celular',
         'fone_residencial',
         'interfone',
         'email',
         'data_aniversario',
         'sexo',
         'responsavel',
         'observacao'
      )
      widgets = {
         'nome': forms.TextInput(attrs={'maxlength': '150', 'size': '80px', 'class': 'control-form'}),
         'nome_preferencial': forms.TextInput(attrs={'maxlength': '50', 'size': '40px', 'class': 'control-form'}),
         'endereco': forms.Textarea(attrs={'cols': '80', 'rows': '3', 'class': 'control-form'}),
         'email': forms.EmailInput(attrs={'maxlength': '150', 'size': '80px', 'class': 'control-form'}),
         'data_aniversario': forms.DateInput(attrs={'type': 'date', 'class': 'control-form'}),
         'sexo': forms.Select(choices=SEXO_CHOICES, attrs={'class': 'control-form'}),
         'observacao': forms.Textarea(attrs={'cols': '80', 'rows': '6', 'class': 'control-form'}),
         'watsapp': forms.TextInput(attrs={'type': 'phone', 'maxlength': '15', 'size': '40px', 'class': 'control-form'})
      }


class ClienteDeleteForm(forms.ModelForm):
   class Meta:
      model = Cliente
      fields = (
         'nome_preferencial',
         'observacao',
         'esta_ativo',
         'esta_excluido',
      )
      widgets = {
         'nome_preferencial': forms.TextInput(attrs={'size': '40px', 'readonly': 'readonly', 'class': 'control-form'}),
         'observacao': forms.Textarea(attrs={'cols': 80, 'rows': 6, 'class': 'control-form'}),
      }


class ClienteDetailForm(forms.ModelForm):
   class Meta:
      model = Cliente
      fields = (
         'nome',
         'nome_preferencial',
         'endereco',
         'watsapp',
         'celular',
         'fone_residencial',
         'interfone',
         'email',
         'data_aniversario',
         'sexo',
         'responsavel',
         'observacao'
      )


class ClienteActiveForm(forms.ModelForm):
   class Meta:
      model = Cliente
      fields = (
         'nome_preferencial',
         'esta_ativo',
         'observacao'
      )
      widgets = {
         'nome_preferencial': forms.TextInput(attrs={'size': '40px', 'readonly': 'readonly', 'class': 'control-form'}),
         'observacao': forms.Textarea(attrs={'cols': 80, 'rows': 6, 'class': 'control-form'}),
      }

   def save(self, commit=True):
      instance = super(ClienteActiveForm, self).save(commit=False)
      instance.esta_ativo = not instance.esta_ativo
      if instance.esta_ativo:
         instance.ativado_em = timezone.now()
      else:
         instance.desativado_em = timezone.now()
      if commit:
         instance.save()
      return instance


class ClienteBlockForm(forms.ModelForm):
   class Meta:
      model = Cliente
      fields = (
         'esta_ativo',
         'esta_bloqueado',
         'nome_preferencial',
         'bloqueado_em',
         'motivo_bloqueio'
      )
      widgets = {
         'nome_preferencial': forms.TextInput(attrs={'size': '40px', 'readonly': 'readonly', 'class': 'control-form'}),
         'motivo_bloqueio': forms.Textarea(
            attrs={'required': 'required', 'cols': '80', 'rows': '6', 'class': 'control-form'}),
      }

   def save(self, commit=True):
      instance = super(ClienteBlockForm, self).save(commit=False)
      instance.esta_ativo = False
      instance.esta_bloqueado = True
      instance.bloqueado_em = timezone.now()
      if commit:
         instance.save()
      return instance
