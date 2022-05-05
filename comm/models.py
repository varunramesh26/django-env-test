from operator import mod
from pyexpat import model
from re import M
from django.db import models

class FarmerInfo(models.Model):
    name = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    crop = models.CharField(max_length=255)