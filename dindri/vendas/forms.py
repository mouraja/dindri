from django import forms
from django.forms.models import inlineformset_factory
from vendas.models import TipoContato, Venda, VendaProduto, Reposicao, ReposicaoProduto


class TipoContatoForm(forms.ModelForm):
   class Meta:
      model = TipoContato
      fields = '__all__'


class VendaForm(forms.ModelForm):
   class Meta:
      model = Venda
      fields = '__all__'


class ReposicaoForm(forms.ModelForm):
   class Meta:
      model = Reposicao
      fields = '__all__'


VendaProdutoFormSet = inlineformset_factory(Venda, VendaProduto, form=VendaForm)
ReposicaoProdutoFormSet = inlineformset_factory(Reposicao, ReposicaoProduto, form=ReposicaoForm)
