from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MascotaSerializer
from django.shortcuts import get_object_or_404

from .models import Mascota




# Create your views here.
def home(request):
    return HttpResponse('Hello World')

@api_view(['GET', 'POST'])
def api_categorias(request):
    if request.method == 'GET':
        categorias = Mascota.objects.all().order_by('id')
        serializer = MascotaSerializer(categorias, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_categorias_detail(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)

    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MascotaSerializer(mascota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','PATCH','DELETE'])
def detalle_categorias(request, id):
    try:
        mascota = Mascota.objects.get(pk=id)
    except Mascota.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    if request.method in ['PUT','PATCH']:
        serializer = MascotaSerializer(mascota, data=request.data, partial=(request.method == 'PATCH'))

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)