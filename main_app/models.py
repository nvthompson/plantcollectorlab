from django.db import models
from django.urls import reverse

# Create your models here.
WATER = (
    ('M', 'Morning'),
    ('N', 'Night')
)

class Plant(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

class Watering(models.Model):
    date = models.DateField('watering date')
    water = models.CharField(
        max_length=1,
        choices=WATER,
        default=WATER[0][0]
    )

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_water_display()} on {self.date}"

    class Meta:
        ordering = ['-date']