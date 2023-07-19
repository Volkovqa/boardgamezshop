from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', load_home),
    path('contacts/', load_contacts),
    path('<int:pk>/prod_card/', prod_card, name='prod_card'),
    path('base/', base)
]
