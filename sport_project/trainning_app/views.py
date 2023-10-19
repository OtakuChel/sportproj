from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import BodySize
from .forms import BodySizeForm
# Create your views here.


class MainPage(TemplateView):
    template_name = 'trainning_app/main_page.html'

class AddBodySize(CreateView):
    model = BodySize
    #fields = '__all__'
    form_class = BodySizeForm
    template_name = 'trainning_app/add_size.html'
    success_url = '/done'

class DoneView(TemplateView):
    template_name = 'trainning_app/done.html'

class ListBodySize(ListView):
    template_name = 'trainning_app/list_sizes.html'
    model = BodySize
    context_object_name = 'sizes'
    def get_queryset(self):
        queryset = super().get_queryset()
        #filter_qs = queryset.filter()
        return  queryset

class DetailBodySize(DetailView):
    template_name = ''
    model = BodySize
