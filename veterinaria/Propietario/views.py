from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Propietario
from .serializers import PropietarioSerializer


@api_view(['GET', 'POST'])
def api_propietarios(request):
    if request.method == 'GET':
        propietarios = Propietario.objects.all().order_by('nombre')
        serializer = PropietarioSerializer(propietarios, many=True)
        return Response(serializer.data)

    serializer = PropietarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
