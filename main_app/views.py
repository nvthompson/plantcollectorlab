from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import Plant

# Create your views here.
class Plant:
    def __init__(self, name, type, color, description):
        self.name = name
        self.type = type
        self.color = color
        self.description = description
        
plants = [
    Plant('Sunflower', 'flower', 'yellow', 'looks nice on a summers day'),
    Plant('Rose', 'flower', ' red', 'perfect for valentines'),
    Plant('Cactus', 'succulent', 'green', 'be careful they are prickly')
    ]

def home(request):
    return HttpResponse('<h1>Plants thrive in good environments</h1>')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {'plants': plants})

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'