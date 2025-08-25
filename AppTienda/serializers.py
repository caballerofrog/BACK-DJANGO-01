from rest_framework import serializers
from .models import Producto, Categoria



class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)  
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), source='categoria', write_only=True
    )

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'unidad', 'precio', 'categoria', 'categoria_id', 'estado', 'fecha_ingreso', 'imagen']
