# Solo valida el rol
from rest_framework import viewsets, permissions
from .models import Proyecto
from .serializers import ProyectoSerializer
from security.models import UsuarioRol

class ProyectoPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        # Define roles y permisos necesarios por tipo de método HTTP
        method_role_perms = {
            'GET': ('Leer', ['Gerente', 'Administrador']),
            'POST': ('Crear', ['Gerente', 'Administrador']),
            'DELETE': ('Eliminar', ['Gerente', 'Administrador']),
            'PUT': ('Actualizar', ['Gerente', 'Administrador']),
            'PATCH': ('Actualizar', ['Gerente', 'Administrador'])
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

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [ProyectoPermission]
