from django.urls import path

from mailer.apps import MailerConfig
from mailer.views import *

app_name = MailerConfig.name
urlpatterns = [
    path('', ...,),
]