from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('plants/<int:plant_id>/add_watering/', views.add_watering, name='add_watering'),
    path('containers/', views.ContainerList.as_view(), name='containers_index'),
    path('containers/<int:pk>/', views.ContainerDetail.as_view(), name='containers_detail'),
    path('containers/create/', views.ContainerCreate.as_view(), name='containers_create'),
    path('containers/<int:pk>/update/', views.ContainerUpdate.as_view(), name='containers_update'),
    path('containers/<int:pk>/delete/', views.ContainerDelete.as_view(), name='containers_delete'),
    path('plants/<int:plant_id>/assoc_container/<int:container_id>/', views.assoc_container, name='assoc_container'),
]
