from django.db import models

# Create your models here.
class Snake(models.Model):
    common_name = models.CharField(max_length=50)
    species = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
