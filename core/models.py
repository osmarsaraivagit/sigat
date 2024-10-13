from django.db import models
from django.db.models import CharField


class Estados(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'estados'

class Cidades(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'cidades'


class Paises(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'paises'

class Funcoes(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    codigo = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'funcoes'


class Origens(models.Model):
    fk_cidade = models.ForeignKey('Cidades', on_delete=models.PROTECT)
    fk_estado = models.ForeignKey('Estados', on_delete=models.PROTECT)
    fk_pais = models.ForeignKey('Paises', on_delete=models.PROTECT)

    class Meta:

        db_table = 'origens'

class Destinos(models.Model):
    fk_cidade = models.ForeignKey('Cidades', on_delete=models.PROTECT)
    fk_estado = models.ForeignKey('Estados', on_delete=models.PROTECT)
    fk_pais = models.ForeignKey('Paises', on_delete=models.PROTECT)

    class Meta:

        db_table = 'destinos'


class FormaPagamento(models.Model):

    tipo = models.CharField(max_length=100, blank=False, null=False)


    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'forma_pagamento'


class Clientes(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    cnpj = models.CharField(db_column='CNPJ', max_length=60, blank=False, null=False)  # Field name made lowercase.
    ie = models.CharField(max_length=60, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    endereco = models.CharField(max_length=80, blank=False, null=False)
    telefone = models.CharField(max_length=60, blank=False, null=False)
    fk_cidade = models.ForeignKey('Cidades', on_delete=models.PROTECT)
    fk_estado = models.ForeignKey('Estados', on_delete=models.PROTECT)
    data_cadastro = models.DateField(null=True, blank=True)

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
    fk_cidade = models.ForeignKey('Cidades', on_delete=models.PROTECT)
    fk_estado = models.ForeignKey('Estados', on_delete=models.PROTECT)
    fone = models.CharField(max_length=30, blank=False, null=False)
    responsavel = models.CharField(max_length=80, blank=False, null=False)
    data_inicio = models.DateField(null=True, blank=True)

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
    fk_cidade = models.ForeignKey('Cidades', on_delete=models.PROTECT)
    fk_estado = models.ForeignKey('Estados', on_delete=models.PROTECT)
    data_cadastro = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'fornecedores'


class Frotas(models.Model):
    nome_frota = models.CharField(max_length=20, blank=False, null=False)
    fk_empresa = models.ForeignKey('Empresas', on_delete=models.PROTECT)
    fk_situacoes = models.ForeignKey('Situacoes', on_delete=models.PROTECT)
    data_cadastro =models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome_frota

    class Meta:
        db_table = 'frotas'


class Exames(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=False)
    cid = models.CharField(max_length=40, blank=False, null=False)
   
    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'exames'


class Funcionarios(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    cpf = models.CharField(db_column='CPF', max_length=50, blank=False, null=False)  # Field name made lowercase.
    pis = models.CharField(db_column='PIS', max_length=30, blank=False, null=False)  # Field name made lowercase.
    data_admissao = models.DateField(null=False, blank=True)
    data_demissao = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=100, blank=False, null=False)
    endereco = models.CharField(max_length=90, blank=False, null=False)
    funcao = models.ForeignKey('funcoes', on_delete=models.PROTECT)
    telefone = models.CharField(max_length=60, blank=False, null=False)
    fk_cidade = models.ForeignKey('Cidades', on_delete=models.PROTECT)
    fk_estado = models.ForeignKey('Estados', on_delete=models.PROTECT)
    fk_situacoes = models.ForeignKey('situacoes', on_delete=models.PROTECT)
    obs = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'funcionarios'


class LancarBaixaVeiculos(models.Model):
    fk_veiculo = models.ForeignKey('veiculos', on_delete=models.PROTECT)
    data_venda = models.DateField(null=False, blank=True)
    km_final = models.IntegerField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    comprador = models.CharField(max_length=60, blank=False, null=False)
    telefone_comprador = models.CharField(max_length=40, blank=False, null=False)


    class Meta:
        db_table = 'lancar_baixa_veiculos'


class LancarContabilidade(models.Model):
    data = models.DateField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    fk_plano_contas = models.ForeignKey('PlanoContas', on_delete=models.PROTECT)
    fk_documento = models.ForeignKey('Documentos', on_delete=models.PROTECT)
    fk_empresa = models.ForeignKey('Empresas', on_delete=models.PROTECT)
    fk_fornecedor = models.ForeignKey('Fornecedores', on_delete=models.PROTECT)
    fk_veiculo = models.ForeignKey('Veiculos', on_delete=models.PROTECT)

    class Meta:
        db_table = 'lancar_contabilidade'


class LancarFerias(models.Model):
    fk_funcionarios = models.ForeignKey('Funcionarios', on_delete=models.PROTECT)
    data_inicio = models.DateField(null=False, blank=True)
    data_fim = models.DateField(null=False, blank=True)
    ano_referente = models.IntegerField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)


    class Meta:
        db_table = 'lancar_ferias'


class LancarFinanceiroViagens(models.Model):
    fk_lancar_viagens = models.ForeignKey('LancarViagens', on_delete=models.PROTECT)
    data = models.DateField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    fk_plano_contas = models.ForeignKey('PlanoContas', on_delete=models.PROTECT)
    fk_documento = models.ForeignKey('Documentos', on_delete=models.PROTECT)
    fk_empresa = models.ForeignKey('Empresas', on_delete=models.PROTECT)
    fk_fornecedor = models.ForeignKey('Fornecedores', on_delete=models.PROTECT)
  

    class Meta:
        db_table = 'lancar_financeiro_viagens'


class LancarViagens(models.Model):
    crtc = models.CharField(max_length=30, blank=False, null=False)
    data = models.DateField(null=False, blank=True)
    fk_frota = models.ForeignKey('Frotas', on_delete=models.PROTECT)
    fk_motorista = models.ForeignKey('Funcionarios', on_delete=models.PROTECT)
    fk_origem = models.ForeignKey('Origens', on_delete=models.PROTECT)
    fk_destino = models.ForeignKey('Destinos', on_delete=models.PROTECT)
    kminicial = models.IntegerField(db_column='kmInicial')  # Field name made lowercase.
    litragem = models.FloatField(null=False, blank=True)
    qtdeveiculos = models.IntegerField(null=False, blank=True)
    fk_empresa = models.ForeignKey('Empresas', on_delete=models.PROTECT)
    obs = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.crtc


    class Meta:
        db_table = 'lancar_viagens'


class PlanoContas(models.Model):
    conta = models.IntegerField(null=False, blank=True)
    tipo = models.CharField(max_length=20, blank=False, null=False)
    descricao = models.CharField(max_length=20, blank=False, null=False)
    subconta = models.IntegerField(null=False, blank=True)
    sigla_situacao = models.CharField(max_length=1, blank=False, null=False)
    saldo = models.DecimalField(max_digits=12, decimal_places=2)

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
    fk_tipo_veiculo = models.ForeignKey('TiposVeiculos', on_delete=models.PROTECT)
    marca = models.CharField(max_length=80, blank=False, null=False)
    modelo = models.CharField(max_length=80, blank=False, null=False)
    ano = models.IntegerField(null=False, blank=True)
    data_fabricacao = models.DateField(null=False, blank=True)
    renavam = models.IntegerField(null=False, blank=True)
    placas = models.CharField(max_length=80, blank=False, null=False)
    datacompra = models.DateField('data', null=False, blank=True)  # Field name made lowercase.
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    fk_empresa = models.ForeignKey('Empresas', on_delete=models.PROTECT)
    fk_frota = models.ForeignKey('Frotas', on_delete=models.PROTECT)
    tipo_aquisicao = models.CharField(max_length=50, blank=False, null=False)
    km_inicial = models.IntegerField(null=False, blank=True)
    fk_situacoes = models.ForeignKey('situacoes', on_delete=models.PROTECT)
    obs = models.CharField(max_length=100, blank=False, null=False)


    class Meta:
        db_table = 'veiculos'


class LancarDocVeiculos(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    data_realizado = models.DateField(null=False, blank=True)
    data_vencimento = models.DateField(null=False, blank=True)
    fk_empresa = models.ForeignKey('Empresas', on_delete=models.PROTECT)
    fk_veiculo = models.ForeignKey('Veiculos', on_delete=models.PROTECT)
    obs = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'lancar_doc_veiculos'


class AcertosViagens(models.Model):
    fk_lancar_viagens = models.ForeignKey('LancarViagens', on_delete=models.PROTECT)
    data_acerto = models.DateField(null=False, blank=True)
    km_final = models.IntegerField(null=False, blank=True)
    valor = models.DecimalField(max_digits=11, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    fk_plano_contas = models.ForeignKey('PlanoContas', on_delete=models.PROTECT)
    fk_forma_pagamento = models.ForeignKey('FormaPagamento', on_delete=models.PROTECT)

    def __str__(self):
        return self.data_acerto


    class Meta:

        db_table = 'acertos_viagens'

