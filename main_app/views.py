from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant

# Create your views here.
# class Plant:
#     def __init__(self, name, type, color, description):
#         self.name = name
#         self.type = type
#         self.color = color
#         self.description = description
        
# plants = [
#     Plant('Sunflower', 'flower', 'yellow', 'looks nice on a summers day'),
#     Plant('Rose', 'flower', ' red', 'perfect for valentines'),
#     Plant('Cactus', 'succulent', 'green', 'be careful they are prickly')
#     ]

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()  
    return render(request, 'plants/index.html', {'plants': plants})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', { 'plant': plant })

class PlantCreate(CreateView):
    model = Plant
    fields = ('name', 'type', 'color', 'description')


class PlantUpdate(UpdateView):
  model = Plant
  fields = ('name', 'type', 'color', 'description')

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'