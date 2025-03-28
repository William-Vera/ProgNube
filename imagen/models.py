from django.db import models
import uuid

class Imagen(models.Model):
    # Definición de campos del modelo
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    nombre = models.CharField(
        max_length=200, 
        verbose_name="Nombre de la Imagen"
    )
    tipo_detectado = models.CharField(
        max_length=100, 
        verbose_name="Tipo Detectado"
    )
    descripcion = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Descripción"
    )
    archivo = models.FileField(
        upload_to='imagenes/', 
        verbose_name="Archivo de Imagen"
    )
    

    def __str__(self):
        return self.nombre
