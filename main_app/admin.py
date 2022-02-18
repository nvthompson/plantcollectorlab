from django.contrib import admin
from .models import Plant, Watering, Container

# Register your models here.
admin.site.register(Plant)
admin.site.register(Watering)
admin.site.register(Container)