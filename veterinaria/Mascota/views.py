from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mascota
from .serializers import MascotaSerializer


@api_view(['GET', 'POST'])
def api_mascotas(request):
    if request.method == 'GET':
        mascotas = Mascota.objects.all().order_by('nombre')
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)

    serializer = MascotaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_mascota_detail(request, id):
    mascota = get_object_or_404(Mascota, pk=id)

    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    if request.method in ['PUT', 'PATCH']:
        serializer = MascotaSerializer(
            mascota,
            data=request.data,
            partial=(request.method == 'PATCH'),
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    mascota.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
