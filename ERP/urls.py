from django.contrib import admin
from django.urls import path, include
from security.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('security/', include('security.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/contabilidad/', include('contabilidad.urls')),
    path('api/gestion_proyectos/', include('gestion_proyectos.urls')),
    path('api/inventario/', include('inventario.urls')),
    path('api/rh/', include('rh.urls')),
    path('docs/', include_docs_urls(title='Api documentation')),

]
