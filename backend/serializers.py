
#------------Usuario--------------------

from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'dni', 'idgeneral', 'nombrey_apellido', 'jefe_inmediato', 'cargo', 'area', 'tipo_usurio', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser(
            dni=validated_data['dni'],
            nombrey_apellido=validated_data['nombrey_apellido'],
            idgeneral=validated_data.get('idgeneral', ''),
            jefe_inmediato=validated_data.get('jefe_inmediato', ''),
            cargo=validated_data.get('cargo', ''),
            area=validated_data.get('area', ''),
            tipo_usurio=validated_data.get('tipo_usurio', 'usuario_comun'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class DiarioDePescaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiarioDePesca
        fields = '__all__'

class EmbarcacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embarcaciones
        fields = '__all__'

class EspeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especies
        fields = '__all__'

class ZonaPescaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonaPesca
        fields = '__all__'

class TarifasCostosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarifasCostos
        fields = '__all__'

class ViveresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viveres
        fields = '__all__'

class MecanismosISerializer(serializers.ModelSerializer):
    class Meta:
        model = MecanismosI
        fields = '__all__'