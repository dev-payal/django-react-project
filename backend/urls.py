from django.urls import path, re_path
from backend.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('country/', RandomCountryView.as_view(), name="country"),
    re_path(r'^', TemplateView.as_view(template_name='index.html')),
]