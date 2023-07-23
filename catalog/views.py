from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


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
