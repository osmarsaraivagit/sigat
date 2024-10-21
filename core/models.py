from django.db import models
from django.db.models import CharField


class Estado(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'estado'

class Cidade(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'cidade'


class Pais(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'pais'

class Funcao(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    codigo = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'funcao'


class Origem(models.Model):
    cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT)
    estado = models.ForeignKey('Estado', on_delete=models.PROTECT)
    pais = models.ForeignKey('Pais', on_delete=models.PROTECT)

    class Meta:

        db_table = 'origem'

class Destino(models.Model):
    fk_cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT)
    fk_estado = models.ForeignKey('Estado', on_delete=models.PROTECT)
    fk_pais = models.ForeignKey('Pais', on_delete=models.PROTECT)

    class Meta:

        db_table = 'destino'


class FormaPagamento(models.Model):

    tipo = models.CharField(max_length=100, blank=False, null=False)


    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'forma_pagamento'


class Cliente(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    cnpj = models.CharField(db_column='CNPJ', max_length=60, blank=False, null=False)  # Field name made lowercase.
    ie = models.CharField(max_length=60, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    endereco = models.CharField(max_length=80, blank=False, null=False)
    telefone = models.CharField(max_length=60, blank=False, null=False)
    fk_cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT)
    fk_estado = models.ForeignKey('Estado', on_delete=models.PROTECT)
    data_cadastro = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


    class Meta:

        db_table = 'cliente'


class Documento(models.Model):
    nome_doc = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self):
        return self.nome_doc

    class Meta:

        db_table = 'documento'


class Empresa(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    cnpj = models.CharField(db_column='CNPJ', max_length=80, blank=False, null=False)  # Field name made lowercase.
    ie = models.CharField(max_length=80, blank=False, null=False)
    email = models.CharField(max_length=80, blank=False, null=False)
    endereco = models.CharField(max_length=100, blank=False, null=False)
    fk_cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT)
    fk_estado = models.ForeignKey('Estado', on_delete=models.PROTECT)
    fone = models.CharField(max_length=30, blank=False, null=False)
    responsavel = models.CharField(max_length=80, blank=False, null=False)
    data_inicio = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome



    class Meta:
        db_table = 'empresa'


class Fornecedor(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    cnpj = models.CharField(db_column='CNPJ', max_length=80, blank=False, null=False)  # Field name made lowercase.
    ie = models.CharField(max_length=80, blank=False, null=False)
    email = models.CharField(max_length=80, blank=False, null=False)
    endereco = models.CharField(max_length=80, blank=False, null=False)
    fone = models.CharField(max_length=30, blank=False, null=False)
    responsavel = models.CharField(max_length=80, blank=False, null=False)
    fk_cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT)
    fk_estado = models.ForeignKey('Estado', on_delete=models.PROTECT)
    data_cadastro = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'fornecedor'


class Frota(models.Model):
    nome_frota = models.CharField(max_length=20, blank=False, null=False)
    fk_empresa = models.ForeignKey('Empresa', on_delete=models.PROTECT)
    fk_situacoes = models.ForeignKey('Situacao', on_delete=models.PROTECT)
    data_cadastro =models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome_frota

    class Meta:
        db_table = 'frota'


class Exame(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=False)
    cid = models.CharField(max_length=40, blank=False, null=False)
   
    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'exame'


class Funcionario(models.Model):
    nome = models.CharField(max_length=80, blank=False, null=False)
    cpf = models.CharField(db_column='CPF', max_length=50, blank=False, null=False)  # Field name made lowercase.
    pis = models.CharField(db_column='PIS', max_length=30, blank=False, null=False)  # Field name made lowercase.
    data_admissao = models.DateField(null=False, blank=True)
    data_demissao = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=100, blank=False, null=False)
    endereco = models.CharField(max_length=90, blank=False, null=False)
    fk_funcao = models.ForeignKey('Funcao', on_delete=models.PROTECT)
    telefone = models.CharField(max_length=60, blank=False, null=False)
    fk_cidade = models.ForeignKey('Cidade', on_delete=models.PROTECT)
    fk_estado = models.ForeignKey('Estado', on_delete=models.PROTECT)
    fk_situacoes = models.ForeignKey('situacao', on_delete=models.PROTECT)
    obs = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'funcionario'


class LancarBaixaVeiculo(models.Model):
    fk_veiculo = models.ForeignKey('veiculo', on_delete=models.PROTECT)
    data_venda = models.DateField(null=False, blank=True)
    km_final = models.IntegerField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    comprador = models.CharField(max_length=60, blank=False, null=False)
    telefone_comprador = models.CharField(max_length=40, blank=False, null=False)


    class Meta:
        db_table = 'lancar_baixa_veiculo'


class LancarContabilidade(models.Model):
    data = models.DateField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    fk_plano_conta = models.ForeignKey('PlanoConta', on_delete=models.PROTECT)
    fk_documento = models.ForeignKey('Documento', on_delete=models.PROTECT)
    fk_empresa = models.ForeignKey('Empresa', on_delete=models.PROTECT)
    fk_fornecedor = models.ForeignKey('Fornecedor', on_delete=models.PROTECT)
    fk_veiculo = models.ForeignKey('Veiculo', on_delete=models.PROTECT)

    class Meta:
        db_table = 'lancar_contabilidade'


class LancarFerias(models.Model):
    fk_funcionario = models.ForeignKey('Funcionario', on_delete=models.PROTECT)
    data_inicio = models.DateField(null=False, blank=True)
    data_fim = models.DateField(null=False, blank=True)
    ano_referente = models.IntegerField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)


    class Meta:
        db_table = 'lancar_ferias'


class LancarFinanceiroViagem(models.Model):
    fk_lancar_viagem = models.ForeignKey('LancarViagem', on_delete=models.PROTECT)
    data = models.DateField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    fk_plano_conta = models.ForeignKey('PlanoConta', on_delete=models.PROTECT)
    fk_documento = models.ForeignKey('Documento', on_delete=models.PROTECT)
    fk_empresa = models.ForeignKey('Empresa', on_delete=models.PROTECT)
    fk_fornecedor = models.ForeignKey('Fornecedor', on_delete=models.PROTECT)
  

    class Meta:
        db_table = 'lancar_financeiro_viagem'


class LancarViagem(models.Model):
    crtc = models.CharField(max_length=30, blank=False, null=False)
    data = models.DateField(null=False, blank=True)
    fk_frota = models.ForeignKey('Frota', on_delete=models.PROTECT)
    fk_motorista = models.ForeignKey('Funcionario', on_delete=models.PROTECT)
    fk_origem = models.ForeignKey('Origem', on_delete=models.PROTECT)
    fk_destino = models.ForeignKey('Destino', on_delete=models.PROTECT)
    kminicial = models.IntegerField(db_column='kmInicial')  # Field name made lowercase.
    litragem = models.FloatField(null=False, blank=True)
    qtdeveiculos = models.IntegerField(null=False, blank=True)
    fk_empresa = models.ForeignKey('Empresa', on_delete=models.PROTECT)
    obs = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.crtc


    class Meta:
        db_table = 'lancar_viagem'


class PlanoConta(models.Model):
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
        db_table = 'plano_conta'


class Situacao(models.Model):
    tipo_nome = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_nome

    class Meta:
        db_table = 'situacao'


class TipoVeiculo(models.Model):
    tipo_veiculo = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.tipo_veiculo

    class Meta:
        db_table = 'tipo_veiculo'


class Veiculo(models.Model):
    fk_tipo_veiculo = models.ForeignKey('TipoVeiculo', on_delete=models.PROTECT)
    marca = models.CharField(max_length=80, blank=False, null=False)
    modelo = models.CharField(max_length=80, blank=False, null=False)
    ano = models.IntegerField(null=False, blank=True)
    data_fabricacao = models.DateField(null=False, blank=True)
    renavam = models.IntegerField(null=False, blank=True)
    placas = models.CharField(max_length=80, blank=False, null=False)
    datacompra = models.DateField('data', null=False, blank=True)  # Field name made lowercase.
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    fk_empresa = models.ForeignKey('Empresa', on_delete=models.PROTECT)
    fk_frota = models.ForeignKey('Frota', on_delete=models.PROTECT)
    tipo_aquisicao = models.CharField(max_length=50, blank=False, null=False)
    km_inicial = models.IntegerField(null=False, blank=True)
    fk_situacoes = models.ForeignKey('situacao', on_delete=models.PROTECT)
    obs = models.CharField(max_length=100, blank=False, null=False)


    class Meta:
        db_table = 'veiculo'


class LancarDocVeiculo(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    data_realizado = models.DateField(null=False, blank=True)
    data_vencimento = models.DateField(null=False, blank=True)
    fk_empresa = models.ForeignKey('Empresa', on_delete=models.PROTECT)
    fk_veiculo = models.ForeignKey('Veiculo', on_delete=models.PROTECT)
    obs = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'lancar_doc_veiculo'


class AcertoViagem(models.Model):
    fk_lancar_viagem = models.ForeignKey('LancarViagem', on_delete=models.PROTECT)
    data_acerto = models.DateField(null=False, blank=True)
    km_final = models.IntegerField(null=False, blank=True)
    valor = models.DecimalField(max_digits=11, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    fk_plano_conta = models.ForeignKey('PlanoConta', on_delete=models.PROTECT)
    fk_forma_pagamento = models.ForeignKey('FormaPagamento', on_delete=models.PROTECT)

    def __str__(self):
        return self.data_acerto


    class Meta:

        db_table = 'acerto_viagem'

