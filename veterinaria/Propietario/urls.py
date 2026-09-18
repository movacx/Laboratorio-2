from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_propietarios, name='api_propietarios'),
]
