from rest_framework import serializers
from .models import (
    Imovel,
    Locador,
    Locatario,
    Fiador,
    Intermediario,
    Contrato,
    Pagamento,
    Manutencao,
    Documento
)

# -----------------------------------------------------------------------------
# 1. SERIALIZER PARA IMÓVEIS
# -----------------------------------------------------------------------------
# Este serializer converte o modelo Imovel para JSON. É o mais simples,
# pois não possui relacionamentos de saída (ForeignKey) para outros modelos.
# -----------------------------------------------------------------------------
class ImovelSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Imovel. Inclui todos os campos.
    """
    class Meta:
        model = Imovel
        fields = '__all__'


# -----------------------------------------------------------------------------
# 2. SERIALIZER PARA LOCADORES
# -----------------------------------------------------------------------------
# Semelhante ao ImovelSerializer, converte o modelo Locador para JSON.
# -----------------------------------------------------------------------------
class LocadorSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Locador.
    """
    class Meta:
        model = Locador
        fields = '__all__'


# -----------------------------------------------------------------------------
# 3. SERIALIZER PARA LOCATÁRIOS
# -----------------------------------------------------------------------------
# Converte o modelo Locatario para JSON.
# -----------------------------------------------------------------------------
class LocatarioSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Locatario.
    """
    class Meta:
        model = Locatario
        fields = '__all__'


# -----------------------------------------------------------------------------
# 4. SERIALIZER PARA CONTRATOS
# -----------------------------------------------------------------------------
# Este é um serializer mais interessante. Ele lida com os relacionamentos
# ForeignKey para Imovel, Locador e Locatário.
# -----------------------------------------------------------------------------
class ContratoSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Contrato.
    Para os campos de chave estrangeira (imovel, locador, locatario),
    em vez de mostrar apenas o ID numérico, podemos mostrar uma representação
    em texto (o resultado do método __str__ do modelo relacionado).
    Isso torna a API muito mais fácil de consumir no frontend.
    """
    # Usamos StringRelatedField para obter a representação em string (__str__)
    # dos modelos relacionados. read_only=True significa que este campo é usado
    # para leitura (GET), não para escrita (POST/PUT).
    imovel = serializers.StringRelatedField(read_only=True)
    locador = serializers.StringRelatedField(read_only=True)
    locatario = serializers.StringRelatedField(read_only=True)

    # Também precisamos incluir os campos de ID para quando formos criar/editar
    # um contrato, pois precisaremos passar os IDs dos objetos relacionados.
    imovel_id = serializers.PrimaryKeyRelatedField(
        queryset=Imovel.objects.all(), source='imovel', write_only=True
    )
    locador_id = serializers.PrimaryKeyRelatedField(
        queryset=Locador.objects.all(), source='locador', write_only=True
    )
    locatario_id = serializers.PrimaryKeyRelatedField(
        queryset=Locatario.objects.all(), source='locatario', write_only=True
    )
    
    class Meta:
        model = Contrato
        # Incluímos todos os campos do modelo, mais os campos de ID para escrita.
        fields = '__all__'


# -----------------------------------------------------------------------------
# 5. SERIALIZER PARA PAGAMENTOS
# -----------------------------------------------------------------------------
# Semelhante ao ContratoSerializer, trata o relacionamento com Contrato.
# -----------------------------------------------------------------------------
class PagamentoSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Pagamento.
    """
    contrato = serializers.StringRelatedField(read_only=True)
    contrato_id = serializers.PrimaryKeyRelatedField(
        queryset=Contrato.objects.all(), source='contrato', write_only=True
    )

    class Meta:
        model = Pagamento
        fields = '__all__'


# -----------------------------------------------------------------------------
# 6. SERIALIZER PARA MANUTENÇÃO
# -----------------------------------------------------------------------------
# Trata o relacionamento com Imovel.
# -----------------------------------------------------------------------------
class ManutencaoSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Manutencao.
    """
    imovel = serializers.StringRelatedField(read_only=True)
    imovel_id = serializers.PrimaryKeyRelatedField(
        queryset=Imovel.objects.all(), source='imovel', write_only=True
    )

    class Meta:
        model = Manutencao
        fields = '__all__'


# -----------------------------------------------------------------------------
# 7. SERIALIZER PARA DOCUMENTOS
# -----------------------------------------------------------------------------
# Trata múltiplos relacionamentos opcionais.
# -----------------------------------------------------------------------------
class DocumentoSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Documento.
    """
    imovel = serializers.StringRelatedField(read_only=True)
    locador = serializers.StringRelatedField(read_only=True)
    locatario = serializers.StringRelatedField(read_only=True)
    contrato = serializers.StringRelatedField(read_only=True)

    imovel_id = serializers.PrimaryKeyRelatedField(
        queryset=Imovel.objects.all(), source='imovel', write_only=True, required=False
    )
    locador_id = serializers.PrimaryKeyRelatedField(
        queryset=Locador.objects.all(), source='locador', write_only=True, required=False
    )
    locatario_id = serializers.PrimaryKeyRelatedField(
        queryset=Locatario.objects.all(), source='locatario', write_only=True, required=False
    )
    contrato_id = serializers.PrimaryKeyRelatedField(
        queryset=Contrato.objects.all(), source='contrato', write_only=True, required=False
    )

    class Meta:
        model = Documento
        fields = '__all__'


# -----------------------------------------------------------------------------
# 8. SERIALIZER PARA FIADOR
# -----------------------------------------------------------------------------
# Converte o modelo Fiador para JSON.
# -----------------------------------------------------------------------------
class FiadorSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Manutencao.
    """

    class Meta:
        model = Fiador
        fields = '__all__'


# -----------------------------------------------------------------------------
# 9. SERIALIZER PARA INTERMEDIARIOS
# -----------------------------------------------------------------------------
# Converte o modelo Locatario para JSON.
# -----------------------------------------------------------------------------
class IntermediarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intermediario
        fields = '__all__'