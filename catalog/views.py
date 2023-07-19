from django.shortcuts import render
from catalog.models import Product


def load_home(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/home.html', context)


def load_prod_card(request):  # в карточке товара зашит определенный продукт. я пока не знаю, как туда передавать данные
    items_list = Product.objects.all()
    context = {
        'object_list': items_list
    }
    return render(request, 'catalog/prod_card.html', context)


def sidebar(request):
    return render(request, 'catalog/sidebar.html')


def base(request):
    return render(request, 'catalog/base.html')


def load_contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"New message!\nAuthor's name: {name}\nemail: {email}\nMessage: {message}")
    return render(request, 'catalog/contacts.html')
