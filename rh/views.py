from rest_framework import viewsets, permissions
from .models import Empleado
from .serializers import EmpleadoSerializer
from security.models import UsuarioRol

class PersonalPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        # Define roles y permisos necesarios por tipo de método HTTP
        method_role_perms = {
            'GET': ('Leer', ['Recursos Humanos', 'Gerente', 'Administrador']),
            'POST': ('Crear', ['Recursos Humanos', 'Administrador']),
            'DELETE': ('Eliminar', ['Recursos Humanos', 'Administrador']),
            'PUT': ('Actualizar', ['Recursos Humanos', 'Administrador']),
            'PATCH': ('Actualizar', ['Recursos Humanos', 'Administrador'])
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

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [PersonalPermission]
