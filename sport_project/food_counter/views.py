from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from users.models import User
from .models import Eating, EatingDate
from .forms import EatingForm, EatingDateForm

from django.http import HttpResponseRedirect

# Create your views here.

class AddOrUpdate(TemplateView):
    template_name = 'food_counter/add_or_update.html'

class AddEatingDate(CreateView):
    model = EatingDate
    #fields = '__all__'
    form_class = EatingDateForm
    template_name = 'food_counter/add_eating_date.html'
    success_url = 'add_eating'

    def get_success_url(self):
        self.success_url = self.success_url + f'/{self.__dict__["object"].__repr__()}'
        return super().get_success_url()

    def post(self, request, *args, **kwargs):
        x = request.POST.copy()
        x['user'] = request.user
        request.POST = x
        return super(AddEatingDate, self).post(request, *args, **kwargs)

class AddEating(CreateView):
    model = Eating

    form_class = EatingForm
    template_name = 'food_counter/eating.html'
    success_url = 'done'

    def post(self, request, *args, **kwargs):
        x = request.POST.copy()
        x['date'] = str(kwargs['pk'])
        x['user'] = request.user
        request.POST = x
        return super(AddEating, self).post(request, *args, **kwargs)


class DoneAdd(TemplateView):
    template_name = 'food_counter/done.html'


class ListEatingDates(ListView):
    template_name = 'food_counter/list_dates.html'
    model = EatingDate
    context_object_name = 'dates'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.filter(user=self.request.user)
        return filter_qs


class ListEatings(ListView):
    template_name = 'food_counter/list_eatings.html'
    model = Eating
    context_object_name = 'eatings'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.filter(date=self.kwargs['pk'])
        return filter_qs

class DetailEating(DetailView):
    template_name = 'food_counter/detail_eating.html'
    model = Eating
    context_object_name = 'eating'

class UpdateEating(UpdateView):
    model = Eating
    form_class = EatingForm #То, как будет выглядеть форма
    template_name = 'food_counter/eating.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        #x = request.POST.copy()
        #x['date'] = str(kwargs['pk'])
        #request.POST = x
        return super(UpdateEating, self).post(request, *args, **kwargs)

def delete_eating(request, pk: int):
    Eating.objects.filter(id=pk).delete()
    return render(request, 'food_counter/done_delete.html')



#class AddEating(UpdateView):
#    model = Eating
#    #fields = '__all__'
#    form_class = EatingForm
#    template_name = 'food_counter/eating.html'
#    success_url = 'add_date/add_eating/done'
#
#
#class ListBodySize(ListView):
#    template_name = 'food_counter/list_dates.html'
#    model = BodySize
#    context_object_name = 'sizes'
#    def get_queryset(self):
#        queryset = super().get_queryset()
#        #filter_qs = queryset.filter()
#        return  queryset
#
#class DetailBodySize(DetailView):
#    template_name = 'food_counter/detail_eating.html'
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