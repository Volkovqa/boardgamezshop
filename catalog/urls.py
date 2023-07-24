from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', ProductListView.as_view()),
    path('contacts/', ContactView.as_view()),
    path('<int:pk>/product_detail/', ProductDetailView.as_view(), name='product_detail'),
]
