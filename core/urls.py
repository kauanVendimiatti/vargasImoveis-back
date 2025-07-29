from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ImovelViewSet,
    LocadorViewSet,
    LocatarioViewSet,
    FiadorViewSet,
    IntermediarioViewSet,
    ContratoViewSet,
    PagamentoViewSet,
    ManutencaoViewSet,
    DocumentoViewSet
)

# O Router do DRF cria automaticamente todas as URLs para um ViewSet.
router = DefaultRouter()
router.register(r'imoveis', ImovelViewSet)
router.register(r'locadores', LocadorViewSet)
router.register(r'locatarios', LocatarioViewSet)
router.register(r'contratos', ContratoViewSet)
router.register(r'pagamentos', PagamentoViewSet)
router.register(r'manutencoes', ManutencaoViewSet)
router.register(r'documentos', DocumentoViewSet)
router.register(r'fiadores', FiadorViewSet)
router.register(r'intermediarios', IntermediarioViewSet)

# As URLs da API são determinadas automaticamente pelo router.
urlpatterns = [
    path('', include(router.urls)),
]