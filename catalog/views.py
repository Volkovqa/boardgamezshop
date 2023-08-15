from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from config import settings


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    # это для эксперимента учебной части
    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     if settings.CACHE_ENABLED:
    #         key = f'subject_{self.object.pk}'
    #         subject_cache = cache.get(key)
    #         if subject_cache is None:
    #             subject_cache = self.object
    #             cache.set(key, subject_cache)
    #     else:
    #         subject_cache = self.object
    #
    #     context_data['subjects'] = subject_cache
    #     return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    login_url = 'users:login'

    def form_valid(self, form):
        self.object = form.save()
        self.object.vendor = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    login_url = 'users:login'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    login_url = 'users:login'


def base(request):
    return render(request, 'catalog/base.html')


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f"New message!\nAuthor's name: {name}\nemail: {email}\nMessage: {message}")
        return super().get_context_data(**kwargs)
