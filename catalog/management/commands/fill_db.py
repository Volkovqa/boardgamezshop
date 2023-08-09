from django.core.management import BaseCommand, call_command

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'fix_data/catalog_data.json')
        call_command('loaddata', 'fix_data/blog_data.json')

