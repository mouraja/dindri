from django import forms
from django.forms.models import inlineformset_factory
from receitas.models import Receita, ReceitaIngrediente, ReceitaInstrucao


class ReceitaForm(forms.ModelForm):
   class Meta:
      model = Receita
      fields = '__all__'


ReceitaIngredienteFormSet = inlineformset_factory(Receita, ReceitaIngrediente, form=ReceitaForm)
ReceitaInstrucaoFormSet = inlineformset_factory(Receita, ReceitaInstrucao, form=ReceitaForm)
