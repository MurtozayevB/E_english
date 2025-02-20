from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, DeleteView, UpdateView)
from admin2.forms import BookModelForm
from apps.models import Book


class AdminBookListView(ListView):
    queryset =Book.objects.all()
    template_name = 'admin/book-list.html'
    context_object_name = 'books'


class AdminBookCreateView(CreateView):
    queryset = Book.objects.all()
    form_class = BookModelForm
    success_url = reverse_lazy('admin-book-list')
    template_name = 'admin/book-list.html'

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

    def form_invalid(self, form):
        messages.error(self.request , "Forma malumoti xato !")
        return super().form_invalid(form)


class AdminBookDeleteView(DeleteView):
    queryset = Book.objects.all()
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('admin-book-list')
    template_name = 'admin/book-list.html'


class AdminBookUpdateView(UpdateView):
    queryset = Book.objects.all()
    form_class = BookModelForm
    success_url = reverse_lazy('admin-book-list')
    template_name = 'admin/book-list.html'

class BookSearchView(ListView):
    queryset = Book.objects.all()
    template_name = 'admin/book-list.html'
    context_object_name = 'books'
    def get_queryset(self):
        query = super().get_queryset()
        search_val = self.request.GET.get('q')
        query = query.filter(name__icontains=search_val)
        return query

