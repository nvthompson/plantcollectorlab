from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant, Container
from .forms import WateringForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()  
    return render(request, 'plants/index.html', {'plants': plants})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    containers_plant_doesnt_have = Container.objects.exclude(id__in = plant.containers.all().values_list('id'))
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', { 
        'plant': plant, 'watering_form': watering_form,
        'containers': containers_plant_doesnt_have
         })

def add_watering(request, plant_id):
  form = WateringForm(request.POST)
  if form.is_valid():
    new_watering = form.save(commit=False)
    new_watering.plant_id = plant_id
    new_watering.save()
  return redirect('detail', plant_id=plant_id)


def assoc_container(request, plant_id, container_id):
  Plant.objects.get(id=plant_id).containers.add(container_id)
  return redirect('detail', plant_id=plant_id)

class PlantCreate(CreateView):
    model = Plant
    fields = ('name', 'type', 'color', 'description')


class PlantUpdate(UpdateView):
  model = Plant
  fields = ('name', 'type', 'color', 'description')

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'

class ContainerCreate(CreateView):
    model = Container
    fields = ('type', 'color')

class ContainerUpdate(UpdateView):
    model = Container
    fields = ('type', 'color')

class ContainerDelete(DeleteView):
    model = Container
    success_url = '/containers/'

class ContainerDetail(DetailView):
    model = Container
    template_name = 'containers/detail.html'

class ContainerList(ListView):
    model = Container
    template_name = 'containers/index.html'