from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import BodySize
from .forms import BodySizeForm
# Create your views here.

class AddBodySize(CreateView):
    model = BodySize
    #fields = '__all__'
    form_class = BodySizeForm
    template_name = 'trainning_app/add_size.html'
    success_url = 'done'

    def post(self, request, *args, **kwargs):
        x = request.POST.copy()
        x['user'] = request.user
        request.POST = x
        return super(AddBodySize, self).post(request, *args, **kwargs)

class DoneView(TemplateView):
    template_name = 'trainning_app/done.html'

class ListBodySize(ListView):
    template_name = 'trainning_app/list_sizes.html'
    model = BodySize
    context_object_name = 'sizes'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.filter(user=self.request.user)
        return filter_qs

class DetailBodySize(DetailView):
    template_name = 'trainning_app/detail_size.html'
    model = BodySize
    context_object_name = 'size'

class BodySizeUpdate(UpdateView):
    model = BodySize
    form_class = BodySizeForm #То, как будет выглядеть форма
    template_name = 'trainning_app/add_size.html'
    success_url = '/done'

def size_delete(request, pk: int):
    BodySize.objects.filter(id=pk).delete()
    return render(request, 'trainning_app/done_delete.html')

