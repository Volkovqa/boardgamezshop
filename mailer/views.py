from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from mailer.forms import MessageForm, MailingSettingsForm, ClientForm
from .models import MailingMessage, MailingSettings, Client, MailingClient


class MailingListView(ListView):
    model = MailingSettings


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailings:mailing_list')


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailings:mailing_list')


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailings:mailing_list')


class MailingClientsListView(ListView):
    model = MailingClient

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['clients'] = Client.objects.all()
        context_data['mailing_pk'] = self.kwargs.get('pk')

        return context_data


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:clients')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:clients')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:clients')


class MessageListView(ListView):
    model = MailingMessage
    template_name = 'mailer/messages.html'


class MessageCreateView(CreateView):
    model = MailingMessage
    form_class = MessageForm
    template_name = 'mailer/message_form.html'
    success_url = reverse_lazy('mailings:messages')


class MessageUpdateView(UpdateView):
    model = MailingMessage
    form_class = MessageForm
    template_name = 'mailer/message_form.html'
    success_url = reverse_lazy('mailings:messages')


class MessageDeleteView(DeleteView):
    model = MailingMessage
    template_name = 'mailer/message_confirm_delete.html'
    success_url = reverse_lazy('mailings:messages')


def toggle_client(request, pk, client_pk):
    if MailingClient.objects.filter(
            client_id=client_pk,
            settings_id=pk
    ).exists():
        MailingClient.objects.filter(
            client_id=client_pk,
            settings_id=pk
        ).delete()
    else:
        MailingClient.objects.create(client_id=client_pk, settings_id=pk)

    return redirect(reverse('mailings:mailing_clients', args=[pk]))
