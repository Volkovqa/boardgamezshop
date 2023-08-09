from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='volkovqa96@gmail.com',
            first_name='Admin',
            last_name='Volkov',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('odmen111')
        user.save()
