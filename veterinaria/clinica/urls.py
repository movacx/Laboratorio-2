from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home_clinica'),
    path('api/mascotas/', include('Mascota.urls')),
    path('api/propietarios/', include('Propietario.urls')),
    path('api/consultas/', views.api_consultas, name='api_consultas'),
    path('api/perfil/', views.perfil, name='perfil'),
    path('api/estadisticas/', views.estadisticas, name='estadisticas'),
    path('api/sesion/', views.sesion, name='sesion'),
]
