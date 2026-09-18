from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_mascotas, name='api_mascotas'),
    path('<int:id>/', views.api_mascota_detail, name='api_mascota_detail'),
]
