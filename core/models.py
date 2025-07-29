from django.db import models

# -----------------------------------------------------------------------------
# 1. MODELO DE IMÓVEIS
# -----------------------------------------------------------------------------
# Armazena todas as informações essenciais sobre os imóveis.
# -----------------------------------------------------------------------------
class Imovel(models.Model):
    """
    Representa um imóvel no sistema, com todas as suas características
    físicas, financeiras e de status.
    """
    # --- Opções para campos com escolhas predefinidas (choices) ---
    TIPO_IMOVEL_CHOICES = [
        ('Casa', 'Casa'),
        ('Apartamento', 'Apartamento'),
        ('Sala Comercial', 'Sala Comercial'),
        ('Prédio Comercial', 'Prédio Comercial'),
        ('Terreno', 'Terreno'),
        ('Galpão', 'Galpão'),
    ]
    STATUS_IMOVEL_CHOICES = [
        ('Disponível', 'Disponível'),
        ('Alugado', 'Alugado'),
        ('Vendido', 'Vendido'),
        ('Em Manutenção', 'Em Manutenção'),
        ('Inativo', 'Inativo'),
    ]

    # --- Campos do Modelo (ATUALIZADOS) ---
    # Dados Principais
    tipo_imovel = models.CharField(max_length=50, choices=TIPO_IMOVEL_CHOICES, verbose_name="Tipo de Imóvel")
    endereco = models.CharField(max_length=255, verbose_name="Endereço Completo")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição Detalhada")
    status_imovel = models.CharField(max_length=50, choices=STATUS_IMOVEL_CHOICES, default='Disponível', verbose_name="Status do Imóvel")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    
    # Características Físicas
    area_util = models.PositiveIntegerField(verbose_name="Área Útil (m²)")
    area_total = models.PositiveIntegerField(blank=True, null=True, verbose_name="Área Total (m²)")
    andar = models.IntegerField(blank=True, null=True, verbose_name="Andar")
    numero_quartos = models.PositiveIntegerField(default=0, verbose_name="Nº de Quartos")
    numero_banheiros = models.PositiveIntegerField(default=1, verbose_name="Nº de Banheiros")
    vagas_garagem = models.PositiveIntegerField(default=0, verbose_name="Vagas de Garagem")

    # NOVOS CAMPOS: Códigos e Condomínio
    codigo_energia = models.CharField(max_length=100, blank=True, null=True, verbose_name="Código de Energia")
    codigo_agua = models.CharField(max_length=100, blank=True, null=True, verbose_name="Código de Água")
    administradora_condominio = models.CharField(max_length=255, blank=True, null=True, verbose_name="Administradora do Condomínio")
    condominio_valor = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Valor do Condomínio")

    # NOVOS CAMPOS: Dados de Aquisição e Venda
    data_aquisicao = models.DateField(blank=True, null=True, verbose_name="Data de Aquisição do Imóvel")
    data_venda = models.DateField(blank=True, null=True, verbose_name="Data da Venda")
    valor_aquisicao = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Valor de Aquisição")
    imposto_venda = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Imposto sobre a Venda")
    valor_liquido_venda = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Valor Líquido da Venda")
    
    # Valores de Locação
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor do Aluguel")
    valor_liquido_aluguel = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Valor Líquido do Aluguel")
    iptu_valor = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Valor do IPTU")
    
    # NOVOS CAMPOS: Seguro do Imóvel
    seguro_vencimento = models.DateField(blank=True, null=True, verbose_name="Vencimento do Seguro")
    seguro_corretora = models.CharField(max_length=255, blank=True, null=True, verbose_name="Corretora do Seguro")
    seguro_seguradora = models.CharField(max_length=255, blank=True, null=True, verbose_name="Seguradora")
    seguro_valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Valor do Seguro")

    # --- NOVOS CAMPOS: CERTIFICADOS COMERCIAIS ---
    avcb_codigo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Código AVCB")
    avcb_emissao = models.DateField(blank=True, null=True, verbose_name="Emissão AVCB")
    avcb_vencimento = models.DateField(blank=True, null=True, verbose_name="Vencimento AVCB")
    vencimento_extintores = models.DateField(blank=True, null=True, verbose_name="Vencimento dos Extintores")
    vencimento_dedetizacao = models.DateField(blank=True, null=True, verbose_name="Vencimento da Dedetização")
    vencimento_caixa_dagua = models.DateField(blank=True, null=True, verbose_name="Vencimento Certificado Caixa d'Água")


    # Campo de Imagens (placeholder)
    imagens = models.CharField(max_length=255, blank=True, null=True, help_text="Caminho ou URL para as imagens")

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"
        ordering = ['-data_cadastro']

    def __str__(self):
        return f"{self.tipo_imovel} - {self.endereco}"


# -----------------------------------------------------------------------------
# 2. MODELO DE LOCADORES (PROPRIETÁRIOS)
# -----------------------------------------------------------------------------
class Locador(models.Model):
    """
    Representa o proprietário de um ou mais imóveis.
    """
    TIPO_DOCUMENTO_CHOICES = [('CPF', 'CPF'), ('CNPJ', 'CNPJ')]
    TIPO_PESSOA_CHOICES = [('Física', 'Física'), ('Jurídica', 'Jurídica')]

    nome = models.CharField(max_length=255, verbose_name="Nome Completo")
    email = models.EmailField(max_length=255, unique=True, verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    profissao = models.CharField(max_length=100, verbose_name="Profissão", null=True, blank=True)
    tipo_pessoa = models.CharField(max_length=10, choices=TIPO_PESSOA_CHOICES, default='Física')
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES, default='CPF')
    cpf_cnpj = models.CharField(max_length=18, unique=True, verbose_name="CPF/CNPJ")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    dados_bancarios = models.TextField(blank=True, null=True, verbose_name="Dados Bancários")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    class Meta:
        verbose_name = "Locador"
        verbose_name_plural = "Locadores"

    def __str__(self):
        return self.nome


# -----------------------------------------------------------------------------
# 3. MODELO DE LOCATÁRIOS (INQUILINOS)
# -----------------------------------------------------------------------------
class Locatario(models.Model):
    """
    Representa o inquilino de um imóvel.
    """
    TIPO_DOCUMENTO_CHOICES = [('CPF', 'CPF'), ('CNPJ', 'CNPJ')]
    TIPO_PESSOA_CHOICES = [('Física', 'Física'), ('Jurídica', 'Jurídica')]

    nome = models.CharField(max_length=255, verbose_name="Nome Completo")
    email = models.EmailField(max_length=255, unique=True, verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    profissao = models.CharField(max_length=100, verbose_name="Profissão", null=True, blank=True)
    tipo_pessoa = models.CharField(max_length=10, choices=TIPO_PESSOA_CHOICES, default='Física')
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES, default='CPF')
    cpf_cnpj = models.CharField(max_length=18, unique=True, verbose_name="CPF/CNPJ")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    dados_bancarios = models.TextField(blank=True, null=True, verbose_name="Dados Bancários")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    
    class Meta:
        verbose_name = "Locatário"
        verbose_name_plural = "Locatários"

    def __str__(self):
        return self.nome


# -----------------------------------------------------------------------------
# 4. MODELO DE CONTRATOS DE LOCAÇÃO
# -----------------------------------------------------------------------------
# Este é um modelo central, que conecta Imóvel, Locador e Locatário.
# -----------------------------------------------------------------------------
class Contrato(models.Model):
    """
    Representa o vínculo legal entre locador, locatário e imóvel.
    """
    STATUS_CONTRATO_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Encerrado', 'Encerrado'),
        ('Rescindido', 'Rescindido'),
        ('Renovado', 'Renovado'),
    ]

    # --- Relacionamentos (Chaves Estrangeiras / Foreign Keys) ---
    # on_delete=models.PROTECT impede que um imóvel ou pessoa seja deletado se tiver um contrato ativo.
    imovel = models.ForeignKey(Imovel, on_delete=models.PROTECT, related_name='contratos', verbose_name="Imóvel")
    locador = models.ForeignKey(Locador, on_delete=models.PROTECT, related_name='contratos', verbose_name="Locador")
    locatario = models.ForeignKey(Locatario, on_delete=models.PROTECT, related_name='contratos', verbose_name="Locatário")

    # --- Detalhes do Contrato ---
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim")
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor do Aluguel (Contratado)")
    valor_deposito = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Valor do Depósito/Caução")
    status_contrato = models.CharField(max_length=20, choices=STATUS_CONTRATO_CHOICES, default='Ativo', verbose_name="Status do Contrato")
    data_assinatura = models.DateField(verbose_name="Data da Assinatura")
    data_vencimento_pagamento = models.PositiveIntegerField(verbose_name="Dia do Vencimento do Pagamento")
    multa_rescisoria = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor da Multa Rescisória")
    clausulas_especificas = models.TextField(blank=True, null=True, verbose_name="Cláusulas Específicas")

    class Meta:
        verbose_name = "Contrato de Locação"
        verbose_name_plural = "Contratos de Locação"

    def __str__(self):
        return f"Contrato #{self.id} - {self.imovel.endereco}"


# -----------------------------------------------------------------------------
# 5. MODELO DE PAGAMENTOS DE ALUGUEL
# -----------------------------------------------------------------------------
class Pagamento(models.Model):
    """
    Registra cada pagamento de aluguel associado a um contrato.
    """
    FORMA_PAGAMENTO_CHOICES = [
        ('Boleto', 'Boleto'),
        ('Transferência Bancária', 'Transferência Bancária'),
        ('Cartão de Crédito', 'Cartão de Crédito'),
        ('PIX', 'PIX'),
    ]
    STATUS_PAGAMENTO_CHOICES = [
        ('Pago', 'Pago'),
        ('Pendente', 'Pendente'),
        ('Em Atraso', 'Em Atraso'),
    ]

    # on_delete=models.CASCADE faz com que os pagamentos sejam deletados se o contrato for deletado.
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='pagamentos', verbose_name="Contrato")
    
    data_pagamento = models.DateField(verbose_name="Data do Pagamento")
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Pago")
    forma_pagamento = models.CharField(max_length=50, choices=FORMA_PAGAMENTO_CHOICES, verbose_name="Forma de Pagamento")
    status_pagamento = models.CharField(max_length=20, choices=STATUS_PAGAMENTO_CHOICES, default='Pendente', verbose_name="Status")
    multa_juros = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Multa/Juros por Atraso")
    comprovante_pagamento = models.CharField(max_length=255, blank=True, null=True, help_text="Caminho ou URL para o comprovante")

    class Meta:
        verbose_name = "Pagamento de Aluguel"
        verbose_name_plural = "Pagamentos de Aluguel"

    def __str__(self):
        return f"Pagamento de {self.contrato.locatario.nome} - Venc: {self.data_pagamento}"


# -----------------------------------------------------------------------------
# 6. MODELO DE MANUTENÇÃO DE IMÓVEIS
# -----------------------------------------------------------------------------
class Manutencao(models.Model):
    """
    Registra solicitações e históricos de manutenção para um imóvel.
    """
    STATUS_MANUTENCAO_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    ]

    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='manutencoes', verbose_name="Imóvel")
    data_solicitacao = models.DateField(verbose_name="Data da Solicitação")
    descricao = models.TextField(verbose_name="Descrição do Problema")
    status_manutencao = models.CharField(max_length=20, choices=STATUS_MANUTENCAO_CHOICES, default='Pendente', verbose_name="Status")
    data_conclusao = models.DateField(blank=True, null=True, verbose_name="Data de Conclusão")
    custo_manutencao = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Custo da Manutenção")
    responsavel_manutencao = models.CharField(max_length=255, blank=True, null=True, verbose_name="Responsável/Empresa")

    class Meta:
        verbose_name = "Manutenção"
        verbose_name_plural = "Manutenções"

    def __str__(self):
        return f"Manutenção em {self.imovel.endereco} ({self.data_solicitacao})"


# -----------------------------------------------------------------------------
# 7. MODELO DE DOCUMENTOS
# -----------------------------------------------------------------------------
class Documento(models.Model):
    """
    Armazena arquivos e documentos diversos, podendo ser associado
    a um imóvel, locador ou locatário.
    """
    # Relacionamentos opcionais (blank=True, null=True)
    imovel = models.ForeignKey(Imovel, on_delete=models.SET_NULL, related_name='documentos', blank=True, null=True)
    locador = models.ForeignKey(Locador, on_delete=models.SET_NULL, related_name='documentos', blank=True, null=True)
    locatario = models.ForeignKey(Locatario, on_delete=models.SET_NULL, related_name='documentos', blank=True, null=True)
    contrato = models.ForeignKey(Contrato, on_delete=models.SET_NULL, related_name='documentos', blank=True, null=True)

    tipo_documento = models.CharField(max_length=100, verbose_name="Tipo de Documento")
    descricao_documento = models.TextField(verbose_name="Descrição do Documento")
    data_documento = models.DateField(verbose_name="Data do Documento")
    # Novamente, o ideal aqui seria um models.FileField
    arquivo_documento = models.CharField(max_length=255, help_text="Caminho ou URL para o arquivo")

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    def __str__(self):
        return self.tipo_documento


# -----------------------------------------------------------------------------
# 8. MODELO DE FIADORES
# -----------------------------------------------------------------------------
class Fiador(models.Model):
    """
    Representa um fiador em um contrato de locação.
    """
    TIPO_DOCUMENTO_CHOICES = [('CPF', 'CPF'), ('CNPJ', 'CNPJ')]
    TIPO_PESSOA_CHOICES = [('Física', 'Física'), ('Jurídica', 'Jurídica')]

    nome = models.CharField(max_length=255, verbose_name="Nome Completo")
    email = models.EmailField(max_length=255, unique=True, verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    profissao = models.CharField(max_length=100, verbose_name="Profissão", null=True, blank=True)
    tipo_pessoa = models.CharField(max_length=10, choices=TIPO_PESSOA_CHOICES, default='Física')
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES, default='CPF')
    cpf_cnpj = models.CharField(max_length=18, unique=True, verbose_name="CPF/CNPJ")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    dados_bancarios = models.TextField(blank=True, null=True, verbose_name="Dados Bancários")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    class Meta:
        verbose_name = "Fiador"
        verbose_name_plural = "Fiadores"

    def __str__(self):
        return self.nome


# -----------------------------------------------------------------------------
# 9. MODELO DE INTERMEDIÁRIOS
# -----------------------------------------------------------------------------
class Intermediario(models.Model):
    """
    Representa um intermediário/corretor em uma negociação.
    """
    TIPO_DOCUMENTO_CHOICES = [('CPF', 'CPF'), ('CNPJ', 'CNPJ')]
    TIPO_PESSOA_CHOICES = [('Física', 'Física'), ('Jurídica', 'Jurídica')]

    nome = models.CharField(max_length=255, verbose_name="Nome Completo")
    email = models.EmailField(max_length=255, unique=True, verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    profissao = models.CharField(max_length=100, verbose_name="Profissão", null=True, blank=True)
    tipo_pessoa = models.CharField(max_length=10, choices=TIPO_PESSOA_CHOICES, default='Física')
    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES, default='CPF')
    cpf_cnpj = models.CharField(max_length=18, unique=True, verbose_name="CPF/CNPJ")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    dados_bancarios = models.TextField(blank=True, null=True, verbose_name="Dados Bancários")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    class Meta:
        verbose_name = "Intermediário"
        verbose_name_plural = "Intermediários"

    def __str__(self):
        return self.nome