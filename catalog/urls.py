from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', load_home),
    path('contacts/', load_contacts),
    path('prod_card/', load_prod_card)
]
