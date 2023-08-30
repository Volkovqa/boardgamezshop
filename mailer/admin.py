from django.contrib import admin

from mailer.models import Client, MailingSettings, MailingMessage, MailingLog, MailingClient


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('last_name',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('time', 'period', 'status', 'message')
    list_filter = ('status',)


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message')


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('last_try', 'status', 'mailing_service_response', 'settings')
    list_filter = ('status',)


@admin.register(MailingClient)
class MailingClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'settings', 'client')
    list_filter = ('client',)
