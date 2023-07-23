from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', ProductListView.as_view()),
    path('contacts/', ContactView.as_view()),
    path('<int:pk>/prod_card/', ProductDetailView.as_view(), name='prod_card'),
]
