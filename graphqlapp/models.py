from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    specialty = models.CharField(max_length=255, blank=True, null=True)
