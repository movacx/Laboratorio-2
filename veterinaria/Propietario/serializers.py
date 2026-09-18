from rest_framework import serializers
from .models import Propietario


class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = '__all__'

    def validate_identificacion(self, value):
        if not value.strip():
            raise serializers.ValidationError('La identificación es obligatoria.')
        return value

    def validate_nombre(self, value):
        if not value.strip():
            raise serializers.ValidationError('El nombre es obligatorio.')
        return value
