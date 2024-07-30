from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UsuarioRol, Permiso

class UsuarioRolInline(admin.StackedInline):
    model = UsuarioRol
    extra = 1

class UserAdmin(BaseUserAdmin):
    inlines = (UsuarioRolInline,)

class PermisoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Permiso, PermisoAdmin)
admin.site.register(UsuarioRol)