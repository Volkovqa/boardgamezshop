from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('<int:pk>/product_detail/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('create_product', ProductCreateView.as_view(), name='product_create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('<int:pk>/products/', CategoryProductListView.as_view(), name='category_products'),
]
