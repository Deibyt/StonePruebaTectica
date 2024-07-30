# security/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UsuarioRol, Rol
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SlugRelatedField(
        many=True,
        slug_field='nombre',
        queryset=Rol.objects.all(),
        required=False
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'roles']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        roles = validated_data.pop('roles', [])
        user = User.objects.create_user(**validated_data)
        for rol in roles:
            UsuarioRol.objects.create(usuario=user, rol=rol)
        return user
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Obtener roles desde el modelo UsuarioRol
        roles = [usuario_rol.rol.nombre for usuario_rol in UsuarioRol.objects.filter(usuario=user)]
        token['roles'] = roles
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        # Obtener roles desde el modelo UsuarioRol
        roles = [usuario_rol.rol.nombre for usuario_rol in UsuarioRol.objects.filter(usuario=self.user)]
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['roles'] = roles
        return data
