from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, DeleteView, UpdateView)
from admin2.forms import UnitModelForm
from apps.models import Book, Unit


class UnitListView(ListView):
    queryset = Unit.objects.all()
    template_name = 'admin/unit-list.html'
    context_object_name = 'units'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context



class UnitCreateView(CreateView):
    queryset = Unit.objects.all()
    form_class = UnitModelForm
    success_url = reverse_lazy('admin-unit-list')
    template_name = 'admin/unit-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['units'] = Unit.objects.all()
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Forma malumoti xato !")
        return super().form_invalid(form)





class UnitDeleteView(DeleteView):
    queryset = Unit.objects.all()
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('admin-unit-list')
    template_name = 'admin/unit-list.html'


class UnitUpdateView(UpdateView):
    queryset = Unit.objects.all()
    form_class = UnitModelForm
    success_url = reverse_lazy('admin-unit-list')
    template_name = 'admin/unit-list.html'
    pk_url_kwarg = 'pk'


class UnitSearchView(ListView):
    queryset = Unit.objects.all()
    template_name = 'admin/unit-list.html'
    context_object_name = 'units'
    def get_queryset(self):
        query = super().get_queryset()
        search_val = self.request.GET.get('q')
        query = query.filter(name__icontains=search_val)
        return query

