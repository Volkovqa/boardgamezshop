from django.urls import path
from blog.views import *
from blog.apps import BlogConfig

app_name = BlogConfig.name
urlpatterns = [
    # path('', ..., name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
#     path('view/<int:pk>', ..., name='view'),
#     path('edit/<int:pk>', ..., name='edit'),
#     path('delete/<int:pk>', ..., name='delete'),
]
