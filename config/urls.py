"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter
from usuario.router import router as usuario_router

from garagem.views import CategoriaViewSet,AcessorioViewSet,ModeloViewSet,MarcaViewSet,VeiculoViewSet, CorViewSet
from uploader.views import ImageUploadViewSet

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"acessorios", AcessorioViewSet)
router.register(r"modelos", ModeloViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"veiculos", VeiculoViewSet)
router.register(r"cores", CorViewSet)
router.register(r"images", ImageUploadViewSet)

urlpatterns = [
    path("api/", include(usuario_router.urls)),
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include(router.urls)),

]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
