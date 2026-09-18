from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

from .models import ConsultaVeterinaria
from .serializers import ConsultaVeterinariaSerializer
from Mascota.models import Mascota
from Propietario.models import Propietario


def home(request):
    return HttpResponse('API de Gestión Veterinaria activa')


# -------------------------------------------------------------------------

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_consultas(request):
    if request.method == 'GET':
        consultas = ConsultaVeterinaria.objects.all().order_by('-fecha')
        serializer = ConsultaVeterinariaSerializer(consultas, many=True)
        return Response(serializer.data)

    serializer = ConsultaVeterinariaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


# -------------------------------------------------------------------------

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def perfil(request):
    return Response({
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,
    })


# -------------------------------------------------------------------------
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def estadisticas(request):
    return Response({
        'total_propietarios': Propietario.objects.count(),
        'total_mascotas': Mascota.objects.count(),
        'mascotas_activas': Mascota.objects.filter(activo=True).count(),
        'total_consultas': ConsultaVeterinaria.objects.count(),
    })


# -------------------------------------------------------------------------

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def sesion(request):
    contador = request.session.get('contador', 0)
    contador += 1
    request.session['contador'] = contador

    return Response({
        'contador': contador
    })
