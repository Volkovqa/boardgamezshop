from django.shortcuts import render


def load_home(request):
    return render(request, 'catalog/home.html')


def load_contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"New message!\nAuthor's name: {name}\nemail: {email}\nMessage: {message}")
    return render(request, 'catalog/contacts.html')
