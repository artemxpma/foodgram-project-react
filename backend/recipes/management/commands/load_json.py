from django.core.management.base import BaseCommand
import json
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Load JSON data'

    def add_arguments(self, parser):
        parser.add_argument('ingredients.json', type=str)

    def handle(self, *args, **options):
        with open(options['ingredients.json']) as f:
            data = json.load(f)
        for ingredient in data:
            Ingredient.objects.create(**ingredient)
