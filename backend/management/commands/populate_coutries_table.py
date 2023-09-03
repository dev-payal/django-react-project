from typing import Any, Optional
import requests
from django.core.management.base import BaseCommand
from backend.models import Country
from django.conf import settings

"""
A custom management command class that inherits from the base command
and contains a handle method contains the executable code when the command -  python manage.py populate_coutries_table is run.
"""

class Command(BaseCommand):
    help ='Poplulate the table with the data from the given API'
    def handle(self, *args, **options):
        response = requests.get(settings.DATA_API)
        data = response.json()['data']
        [Country.objects.create(name=country["name"], capital=country["capital"]) for country in data]
        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))