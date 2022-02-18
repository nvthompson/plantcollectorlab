from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name