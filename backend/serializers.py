
#------------Usuario--------------------

from rest_framework import serializers
from .models import CustomUser, DiarioDePesca

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