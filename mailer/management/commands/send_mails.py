from django.core.management import BaseCommand
from mailer.services import send_mails


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_mails()
