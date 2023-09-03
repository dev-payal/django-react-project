from django.shortcuts import render
from rest_framework.views import APIView, View
from .serializers import CountrySerializer
from .models import Country
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework import status
import random

# Create your views here.

# API to generate a random country entry from the database table country
class RandomCountryView(APIView):
    def get(self, request):
        countries = Country.objects.all()
        random_country = random.choice(countries)
        serializer = CountrySerializer(random_country)
        return Response(serializer.data)