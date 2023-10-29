from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import Eating, EatingDate
from .forms import EatingForm, EatingDateForm

# Create your views here.

class AddEatingDate(CreateView):
    model = EatingDate
    #fields = '__all__'
    form_class = EatingDateForm
    template_name = 'food_counter/add_eating_date.html'
    success_url = 'add_eating'

class AddEating(CreateView):
    model = Eating
    #fields = '__all__'
    exclude = ['date']
    form_class = EatingForm
    template_name = 'food_counter/eating.html'
    success_url = 'add_eating/done'

#class AddEating(UpdateView):
#    model = Eating
#    #fields = '__all__'
#    form_class = EatingForm
#    template_name = 'food_counter/eating.html'
#    success_url = 'add_date/add_eating/done'
#
#
#class ListBodySize(ListView):
#    template_name = 'food_counter/list_sizes.html'
#    model = BodySize
#    context_object_name = 'sizes'
#    def get_queryset(self):
#        queryset = super().get_queryset()
#        #filter_qs = queryset.filter()
#        return  queryset
#
#class DetailBodySize(DetailView):
#    template_name = 'food_counter/detail_size.html'
#    model = BodySize
#    context_object_name = 'size'
#
#class BodySizeUpdate(UpdateView):
#    model = BodySize
#    form_class = BodySizeForm #То, как будет выглядеть форма
#    template_name = 'food_counter/add_eating_date.html'
#    success_url = '/done'
#
#class SureDelete(DeleteView):
#    model = BodySize
#    form_class = BodySizeForm
#    context_object_name = 'size'
#    template_name = 'food_counter/sure_delete.html'
#    success_url = '/done_delete'
#
#class DoneDelete(TemplateView):
#    template_name = 'food_counter/done_delete.html'