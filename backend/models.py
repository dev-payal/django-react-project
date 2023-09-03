from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=300)
    capital = models.CharField(max_length=500)
    def __str__(self):
        return self.name
