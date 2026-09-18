from rest_framework import serializers
from .models import Mascota


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

    def validate_nombre(self, value):
        if not value.strip():
            raise serializers.ValidationError('El nombre de la mascota es obligatorio.')
        return value

    def validate_peso(self, value):
        if value <= 0:
            raise serializers.ValidationError('El peso debe ser mayor que cero.')
        return value
