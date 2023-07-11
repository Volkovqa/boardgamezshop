from django.urls import path
from catalog.views import load_home, load_contacts

urlpatterns = [
    path('', load_home),
    path('contacts/', load_contacts)
]
