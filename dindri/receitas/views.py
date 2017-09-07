from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from receitas.models import Receita
from receitas.forms import ReceitaForm, ReceitaIngredienteFormSet, ReceitaInstrucaoFormSet


# Create your views here.

# Receitas
class ReceitasHomeView(TemplateView):
   template_name = 'receitas_home.html'


# Receita
class ReceitaListView(ListView):
   model = Receita
   form_class = ReceitaForm
   template_name = 'receita_list.html'


class ReceitaDetailView(DetailView):
   model = Receita
   form_class = ReceitaForm
   template_name = 'receita_detail.html'
   success_url = reverse_lazy('receita_list')


class ReceitaUpdateView(UpdateView):
   model = Receita
   form_class = ReceitaForm
   template_name = 'receita_update.html'
   success_url = reverse_lazy('receita_list')


class ReceitaDeleteView(DeleteView):
   model = Receita
   form_class = ReceitaForm
   template_name = 'receita_delete_confirm.html'
   success_url = reverse_lazy('receita_list')


class ReceitaCreateView(CreateView):
   template_name = 'receita_create.html'
   model = Receita
   form_class = ReceitaForm
   success_url = reverse_lazy('receita_list')

   def get(self, request, *args, **kwargs):
      """
      Handles GET requests and instantiates blank versions of the form
      and its inline formsets.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      receita_ingrediente_form = ReceitaIngredienteFormSet()
      receita_instrucao_form = ReceitaInstrucaoFormSet()
      return self.render_to_response(
         self.get_context_data(
            form=form,
            receita_ingrediente_form=receita_ingrediente_form,
            receita_instrucao_form=receita_instrucao_form,
         )
      )

   def post(self, request, *args, **kwargs):
      """
      Handles POST requests, instantiating a form instance and its inline
      formsets with the passed POST variables and then checking them for
      validity.
      """
      self.object = None
      form_class = self.get_form_class()
      form = self.get_form(form_class)
      receita_ingrediente_form = ReceitaIngredienteFormSet(self.request.POST)
      receita_instrucao_form = ReceitaInstrucaoFormSet(self.request.POST)
      if (form.is_valid() and receita_ingrediente_form.is_valid() and
             receita_instrucao_form.is_valid()):
         return self.form_valid(form, receita_ingrediente_form, receita_instrucao_form)
      else:
         return self.form_invalid(form, receita_ingrediente_form, receita_instrucao_form)

   def form_valid(self, form, receita_ingrediente_form, receita_instrucao_form):
      """
      Called if all forms are valid. Creates a Recipe instance along with
      associated Ingredients and Instructions and then redirects to a
      success page.
      """
      self.object = form.save()
      receita_ingrediente_form.instance = self.object
      receita_ingrediente_form.save()
      receita_instrucao_form.instance = self.object
      receita_instrucao_form.save()
      return HttpResponseRedirect(self.get_success_url())

   def form_invalid(self, form, receita_ingrediente_form, receita_instrucao_form):
      """
      Called if a form is invalid. Re-renders the context data with the
      data-filled forms and errors.
      """
      return self.render_to_response(
         self.get_context_data(
            form=form,
            receita_ingrediente_form=receita_ingrediente_form,
            receita_instrucao_form=receita_instrucao_form,
         )
      )
