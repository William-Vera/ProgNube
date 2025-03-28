from rest_framework import serializers
from .models import Imagen

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = [
            'id', 
            'nombre', 
            'tipo_detectado', 
            'descripcion', 
            'archivo', 
        ]
        read_only_fields = ['id']