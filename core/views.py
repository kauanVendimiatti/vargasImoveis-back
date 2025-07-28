from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework import viewsets
from .models import (
    Imovel,
    Locador,
    Locatario,
    Contrato,
    Pagamento,
    Manutencao,
    Documento
)
from .serializers import (
    ImovelSerializer,
    LocadorSerializer,
    LocatarioSerializer,
    ContratoSerializer,
    PagamentoSerializer,
    ManutencaoSerializer,
    DocumentoSerializer
)

# -----------------------------------------------------------------------------
# Explicação:
# Cada classe abaixo é um 'ViewSet'. Pense nela como um controlador completo
# para um modelo específico. Ela define qual conjunto de dados (queryset)
# e qual tradutor (serializer_class) usar.
# Usamos 'ModelViewSet' porque ele fornece todas as ações CRUD por padrão.
# -----------------------------------------------------------------------------

class AppView(TemplateView):
    template_name = 'index.html'

# --- 1. VIEWSET PARA IMÓVEIS ---
class ImovelViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os imóveis sejam visualizados ou editados.
    """
    queryset = Imovel.objects.all().order_by('-data_cadastro')
    serializer_class = ImovelSerializer


# --- 2. VIEWSET PARA LOCADORES ---
class LocadorViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os locadores sejam visualizados ou editados.
    """
    queryset = Locador.objects.all()
    serializer_class = LocadorSerializer


# --- 3. VIEWSET PARA LOCATÁRIOS ---
class LocatarioViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os locatários sejam visualizados ou editados.
    """
    queryset = Locatario.objects.all()
    serializer_class = LocatarioSerializer


# --- 4. VIEWSET PARA CONTRATOS ---
class ContratoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os contratos sejam visualizados ou editados.
    """
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer


# --- 5. VIEWSET PARA PAGAMENTOS ---
class PagamentoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os pagamentos sejam visualizados ou editados.
    """
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer


# --- 6. VIEWSET PARA MANUTENÇÃO ---
class ManutencaoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que as manutenções sejam visualizadas ou editadas.
    """
    queryset = Manutencao.objects.all()
    serializer_class = ManutencaoSerializer


# --- 7. VIEWSET PARA DOCUMENTOS ---
class DocumentoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os documentos sejam visualizados ou editados.
    """
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer