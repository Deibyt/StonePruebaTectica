from rest_framework import serializers
from .models import Articulo

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'
