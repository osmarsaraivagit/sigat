from django.db import models


class Localidades(models.Model):
    cidade = models.CharField(max_length=50, blank=False, null=False)
    estado = models.CharField(max_length=2, blank=False, null=False)
    pais = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.cidade


    class Meta:

        db_table = 'localidades'


class AcertosViagens(models.Model):
    fk_lancar_viagens = models.ForeignKey('LancarViagens', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=11, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    fk_plano_contas = models.ForeignKey('PlanoContas', on_delete=models.CASCADE)


    def __str__(self):
        return self.fk_plano_contas


    class Meta:

        db_table = 'acertos_viagens'


class Clientes(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    cnpj = models.CharField(db_column='CNPJ', max_length=60, blank=False, null=False)  # Field name made lowercase.
    ie = models.CharField(max_length=60, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    endereco = models.CharField(max_length=80, blank=False, null=False)
    telefone = models.CharField(max_length=60, blank=False, null=False)
    data_cadastro = models.DateField()
    fk_localidades = models.ForeignKey('localidades', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


    class Meta:

        db_table = 'clientes'


class Documentos(models.Model):
    nome_doc = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self):
        return self.nome_doc

    class Meta:

        db_table = 'documentos'


class Empresas(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    cnpj = models.CharField(db_column='CNPJ', max_length=80, blank=False, null=False)  # Field name made lowercase.
    ie = models.CharField(max_length=80, blank=False, null=False)
    email = models.CharField(max_length=80, blank=False, null=False)
    endereco = models.CharField(max_length=100, blank=False, null=False)
    fk_localidades = models.ForeignKey('localidades', on_delete=models.CASCADE)
    fone = models.CharField(max_length=30, blank=False, null=False)
    responsavel = models.CharField(max_length=80, blank=False, null=False)
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome



    class Meta:
        db_table = 'empresas'


class Fornecedores(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    cnpj = models.CharField(db_column='CNPJ', max_length=80, blank=False, null=False)  # Field name made lowercase.
    ie = models.CharField(max_length=80, blank=False, null=False)
    email = models.CharField(max_length=80, blank=False, null=False)
    endereco = models.CharField(max_length=80, blank=False, null=False)
    fone = models.CharField(max_length=30, blank=False, null=False)
    responsavel = models.CharField(max_length=80, blank=False, null=False)
    data_cadastro = models.DateField()
    fk_localidade = models.ForeignKey('localidades', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'fornecedores'


class Frotas(models.Model):
    nome_frota = models.CharField(max_length=20, blank=False, null=False)
    fk_empresa = models.ForeignKey('Empresas', on_delete=models.CASCADE)
    fk_situacoes = models.ForeignKey('Situacoes', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_frota



    class Meta:
        db_table = 'frotas'


class Funcionarios(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    cpf = models.CharField(db_column='CPF', max_length=50, blank=False, null=False)  # Field name made lowercase.
    pis = models.CharField(db_column='PIS', max_length=30, blank=False, null=False)  # Field name made lowercase.
    data_admissao = models.DateField()
    data_demissao = models.DateField()
    email = models.CharField(max_length=100, blank=False, null=False)
    endereco = models.CharField(max_length=90, blank=False, null=False)
    funcao = models.CharField(max_length=60, blank=False, null=False)
    telefone = models.CharField(max_length=60, blank=False, null=False)
    fk_localidade = models.ForeignKey('localidades', on_delete=models.CASCADE)
    fk_situacoes = models.ForeignKey('situacoes', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'funcionarios'


class LancarBaixaVeiculos(models.Model):
    fk_veiculo = models.ForeignKey('veiculos', on_delete=models.CASCADE)
    data_venda = models.DateField()
    km_final = models.IntegerField()
    valor = models.DecimalField(max_digits=11, decimal_places=2, blank=False, null=False)
    comprador = models.CharField(max_length=60, blank=False, null=False)
    telefone_comprador = models.CharField(max_length=40, blank=False, null=False)


    class Meta:
        db_table = 'lancar_baixa_veiculos'


class LancarContabilidade(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=11, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    fk_plano_contas = models.ForeignKey('PlanoContas', on_delete=models.CASCADE)
    fk_documento = models.ForeignKey('Documentos', on_delete=models.CASCADE)
    fk_empresa = models.ForeignKey('Empresas', on_delete=models.CASCADE)
    fk_fornecedor = models.ForeignKey('Fornecedores', on_delete=models.CASCADE)
    fk_veiculo = models.ForeignKey('Veiculos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'lancar_contabilidade'


class LancarFerias(models.Model):
    fk_funcionarios = models.ForeignKey('Funcionarios', on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ano_referente = models.DateField()
    valor = models.DecimalField(max_digits=11, decimal_places=2)


    class Meta:
        db_table = 'lancar_ferias'


class LancarFinanceiroViagens(models.Model):
    fk_lancar_viagens = models.ForeignKey('LancarViagens', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=11, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    fk_plano_contas = models.ForeignKey('PlanoContas', on_delete=models.CASCADE)
    fk_documento = models.ForeignKey('Documentos', on_delete=models.CASCADE)
    fk_empresa = models.ForeignKey('Empresas', on_delete=models.CASCADE)
    fk_fornecedor = models.ForeignKey('Fornecedores', on_delete=models.CASCADE)

    class Meta:
        db_table = 'lancar_financeiro_viagens'


class LancarViagens(models.Model):
    crtc = models.CharField(max_length=30, blank=False, null=False)
    data = models.DateField()
    fk_frota = models.ForeignKey('Frotas', on_delete=models.CASCADE)
    fk_motorista = models.ForeignKey('Funcionarios', on_delete=models.CASCADE)
    fk_destino = models.ForeignKey('Localidades', on_delete=models.CASCADE)
    kmfinal = models.IntegerField(db_column='kmFinal')  # Field name made lowercase.
    kminicial = models.IntegerField(db_column='kmInicial')  # Field name made lowercase.
    litragem = models.FloatField()
    qtdeveiculos = models.IntegerField()
    fk_empresa = models.ForeignKey('Empresas', on_delete=models.CASCADE)

    def __str__(self):
        return self.crtc


    class Meta:
        db_table = 'lancar_viagens'


class PlanoContas(models.Model):
    conta = models.IntegerField()
    tipo = models.CharField(max_length=20, blank=False, null=False)
    descricao = models.CharField(max_length=20, blank=False, null=False)
    subconta = models.IntegerField()
    sigla_situacao = models.CharField(max_length=1, blank=False, null=False)
    saldo = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.conta

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'plano_contas'


class Situacoes(models.Model):
    tipo_nome = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_nome

    class Meta:
        db_table = 'situacoes'


class TiposVeiculos(models.Model):
    tipo_de_veiculo = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.tipo_de_veiculo

    class Meta:
        db_table = 'tipos_veiculos'


class Veiculos(models.Model):
    fk_tipo_veiculo = models.ForeignKey('TiposVeiculos', on_delete=models.CASCADE)
    marca = models.CharField(max_length=80, blank=False, null=False)
    modelo = models.CharField(max_length=80, blank=False, null=False)
    placas = models.CharField(max_length=80, blank=False, null=False)
    datacompra = models.DateField(db_column='dataCompra')  # Field name made lowercase.
    fk_empresa = models.ForeignKey('Empresas', on_delete=models.CASCADE)
    fk_frota = models.ForeignKey('Frotas', on_delete=models.CASCADE)
    tipo_aquisicao = models.CharField(max_length=50, blank=False, null=False)
    km_inicial = models.IntegerField()
    fk_situacoes = models.ForeignKey('situacoes', on_delete=models.CASCADE)


    class Meta:
        db_table = 'veiculos'



