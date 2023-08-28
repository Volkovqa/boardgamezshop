from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, TemplateView
)

from blog.models import Blog
from mailer.forms import MessageForm, MailingSettingsForm, ClientForm, MailingSettingsForManagerForm
from .models import MailingMessage, MailingSettings, Client, MailingClient, MailingLog


class MailingListView(LoginRequiredMixin, ListView):
    model = MailingSettings

    def get_queryset(self):
        """Пользователь видит только свои рассылки"""
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailer.view_mailingsettings'):
            return queryset  # Если есть право доступа, то пользователь видит все рассылки
        return queryset.filter(owner=self.request.user)


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        """ У рассылки появляется 'owner' - авторизированный пользователь """
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailingSettingsUpdateView(UserPassesTestMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailings:mailing_list')

    def test_func(self):
        mailing = self.get_object()
        user = self.request.user
        if mailing.owner == user or user.is_superuser:
            self.form_class = MailingSettingsForm
        elif user.has_perm('mailer.set_status'):
            self.form_class = MailingSettingsForManagerForm
        return user.is_authenticated and (mailing.owner == user or user.has_perm('mailer.set_status'))


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailings:mailing_list')
    permission_required = 'mailer.change_mailingsettings'

    def get_object(self, queryset=None):
        """ Проверка на то, что пользователь не может удалять чужое сообщение """
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class MailingClientsListView(ListView):
    model = MailingClient
    template_name = 'mailer/mailingclient_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(mailing=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['clients'] = Client.objects.filter(owner=self.request.user)
        context_data['mailing_pk'] = self.kwargs.get('pk')

        return context_data


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:clients')

    def form_valid(self, form):
        """ owner для клиента """
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:clients')

    def get_object(self, queryset=None):
        """ Проверка на то, что пользователь не может менять чужого клиента """
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:clients')

    def get_object(self, queryset=None):
        """ Проверка на то, что пользователь не может удалить чужого клиента """
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class MessageListView(LoginRequiredMixin, ListView):
    model = MailingMessage
    template_name = 'mailer/messages.html'

    def get_queryset(self):
        """Пользователь видит только свои сообщения"""
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailer.view_mailingmessage'):
            return queryset  # Если есть право доступа, то пользователь видит все сообщения
        return super().get_queryset().filter(owner=self.request.user)


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = MailingMessage
    form_class = MessageForm
    template_name = 'mailer/message_form.html'
    success_url = reverse_lazy('mailings:messages')

    def form_valid(self, form):
        """ У сообщения появляется 'owner' - авторизированный пользователь """
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingMessage
    form_class = MessageForm
    template_name = 'mailer/message_form.html'
    success_url = reverse_lazy('mailings:messages')

    def get_object(self, queryset=None):
        """ Проверка на то, что пользователь не может менять чужое сообщение """
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingMessage
    template_name = 'mailer/message_confirm_delete.html'
    success_url = reverse_lazy('mailings:messages')

    def get_object(self, queryset=None):
        """ Проверка на то, что пользователь не может удалять чужое сообщение """
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


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


class MailingLogsListView(ListView):
    model = MailingLog

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailer.view_mailinglog'):
            return queryset  # Если есть право доступа, то пользователь видит все рассылки
        return queryset.filter(owner=self.request.user)


class HomePageView(TemplateView):
    template_name = 'mailer/home_page.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count_mailing'] = MailingSettings.objects.all().count()
        context_data['count_mailing_active'] = MailingSettings.objects.filter(
            status=MailingSettings.STATUS_STARTED).count()
        context_data['count_unique_customers'] = Client.objects.distinct().count()
        context_data['blog'] = Blog.objects.all()[:3]
        context_data['title'] = 'Главная страница рассылок'
        return context_data
