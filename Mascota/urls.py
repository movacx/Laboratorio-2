from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home_mascota'),
    path('api/mascota/', views.api_mascotas, name='api_mascota'),
    path('api/mascota/<int:pk>/', views.api_mascota_detail, name='api_mascota_detail'),
    path('api/detalle_mascotas/', views.api_detalle_mascotas, name = 'api_detalle_mascotas'),
]