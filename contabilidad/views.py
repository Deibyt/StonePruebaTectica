from rest_framework import viewsets, permissions
from .models import Transaccion
from .serializers import TransaccionSerializer
from security.models import UsuarioRol

class TransaccionPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        # Define roles y permisos necesarios por tipo de método HTTP
        method_role_perms = {
            'GET': ('Leer', ['Contador', 'Gerente', 'Administrador']),
            'POST': ('Crear', ['Contador', 'Administrador']),
            'DELETE': ('Eliminar', ['Contador', 'Administrador']),
            'PUT': ('Actualizar', ['Contador', 'Administrador']),
            'PATCH': ('Actualizar', ['Contador', 'Administrador'])
        }

        # Obtener el permiso y los roles necesarios para el método actual
        required_perm, allowed_roles = method_role_perms.get(request.method, (None, []))
        
        # Si no hay configuración para este método, denegar permiso
        if not required_perm:
            return False

        # Verificar roles y permisos del usuario
        user_roles = UsuarioRol.objects.filter(usuario=user)
        for ur in user_roles:
            if ur.rol.nombre in allowed_roles:
                user_perms = [perm.nombre for perm in ur.permisos.all()]
                if required_perm in user_perms:
                    return True

        return False

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer
    permission_classes = [TransaccionPermission]
