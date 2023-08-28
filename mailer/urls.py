from django.urls import path

from mailer.apps import MailerConfig
from mailer.views import *

app_name = MailerConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='main'),
    path('create/', MailingSettingsCreateView.as_view(), name='mailing_create'),
    path('update/<int:pk>/', MailingSettingsUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>/', MailingSettingsDeleteView.as_view(), name='mailing_delete'),

    path('mailing/<int:pk>/clients/', MailingClientsListView.as_view(), name='mailing_clients'),
    path('mailing/<int:pk>/clients/add/<int:client_pk>/', toggle_client, name='mailing_clients_toggle'),

    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients/create/', ClientCreateView.as_view(), name='clients_create'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='clients_update'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='clients_delete'),

    path('messages/', MessageListView.as_view(), name='messages'),
    path('messages/create/', MessageCreateView.as_view(), name='messages_create'),
    path('messages/update/<int:pk>/', MessageUpdateView.as_view(), name='messages_update'),
    path('messages/delete/<int:pk>/', MessageDeleteView.as_view(), name='messages_delete'),

    path('mailinglogs/', MailingLogsListView.as_view(), name='mailing_logs'),
]
