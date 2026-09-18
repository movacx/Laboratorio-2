from rest_framework import serializers
from .models import ConsultaVeterinaria


class ConsultaVeterinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaVeterinaria
        fields = '__all__'
        read_only_fields = ['fecha']

    def validate_motivo(self, value):
        if not value.strip():
            raise serializers.ValidationError('El motivo de la consulta es obligatorio.')
        return value

    def validate_costo(self, value):
        if value < 0:
            raise serializers.ValidationError('El costo no puede ser negativo.')
        return value
