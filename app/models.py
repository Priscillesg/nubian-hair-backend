from django.db import models

# Create your models here.

from django.db import models
class Salon(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    def __str__(self):
        return self.name