from django.db import models


class AcertosViagens(models.Model):
    fk_lancar_viagens = models.ForeignKey('LancarViagens', models.DO_NOTHING)
    creditar = models.DecimalField(max_digits=10, decimal_places=2)
    debitar = models.DecimalField(max_digits=10, decimal_places=2)
    historico = models.CharField(max_length=100)
    fk_plano_contas = models.ForeignKey('PlanoContas', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'acertos_viagens'


class Cidades(models.Model):
    id = models.BigAutoField(primary_key=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'cidades'


class Clientes(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    cnpj = models.CharField(db_column='CNPJ', max_length=60)  # Field name made lowercase.
    ie = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=80)
    telefone = models.CharField(max_length=60)
    data_cadastro = models.DateField()
    fk_cidades = models.ForeignKey(Cidades, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clientes'


class Documentos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_doc = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'documentos'


class Empresas(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    cnpj = models.CharField(db_column='CNPJ', max_length=80)  # Field name made lowercase.
    ie = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    endereco = models.CharField(max_length=100)
    fk_cidades = models.ForeignKey(Cidades, models.DO_NOTHING)
    fone = models.CharField(max_length=30)
    responsavel = models.CharField(max_length=80)
    data_inicio = models.DateField()

    class Meta:
        managed = False
        db_table = 'empresas'


class Fornecedores(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    cnpj = models.CharField(db_column='CNPJ', max_length=80)  # Field name made lowercase.
    ie = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    endereco = models.CharField(max_length=80)
    fone = models.CharField(max_length=30)
    responsavel = models.CharField(max_length=80)
    data_cadastro = models.DateField()
    fk_cidades = models.ForeignKey(Cidades, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fornecedores'


class Frotas(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome_frota = models.CharField(max_length=20)
    fk_empresas = models.ForeignKey(Empresas, models.DO_NOTHING)
    fk_situacoes = models.ForeignKey('Situacoes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'frotas'


class Funcionarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    cpf = models.CharField(db_column='CPF', max_length=50)  # Field name made lowercase.
    pis = models.CharField(db_column='PIS', max_length=30)  # Field name made lowercase.
    data_admissao = models.DateField()
    data_demissao = models.DateField()
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=90)
    funcao = models.CharField(max_length=60)
    nome = models.CharField(max_length=80)
    telefone = models.CharField(max_length=60)
    fk_cidades = models.ForeignKey(Cidades, models.DO_NOTHING)
    fk_situacoes = models.ForeignKey('Situacoes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'funcionarios'


class LancarBaixaVeiculos(models.Model):
    id = models.BigAutoField(primary_key=True)
    fk_veiculos = models.ForeignKey('Veiculos', models.DO_NOTHING)
    data_venda = models.DateField()
    km_final = models.IntegerField()
    comprador = models.CharField(max_length=60)
    fone_comprador = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'lancar_baixa_veiculos'


class LancarContabilidade(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.DateField()
    debitar = models.DecimalField(max_digits=10, decimal_places=2)
    creditar = models.DecimalField(max_digits=10, decimal_places=2)
    historico = models.CharField(max_length=100)
    fk_plano_contas = models.ForeignKey('PlanoContas', models.DO_NOTHING)
    fk_documento = models.ForeignKey(Documentos, models.DO_NOTHING)
    fk_empresa = models.ForeignKey(Empresas, models.DO_NOTHING)
    fk_fornecedor = models.ForeignKey(Fornecedores, models.DO_NOTHING)
    fk_veiculos = models.ForeignKey('Veiculos', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lancar_contabilidade'


class LancarFerias(models.Model):
    fk_funiconarios_id = models.BigIntegerField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ano_referente = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'lancar_ferias'


class LancarFinanceiroViagens(models.Model):
    id = models.BigAutoField(primary_key=True)
    fk_lancar_viagens = models.ForeignKey('LancarViagens', models.DO_NOTHING)
    creditar = models.DecimalField(max_digits=8, decimal_places=2)
    debitar = models.DecimalField(max_digits=8, decimal_places=2)
    historico = models.CharField(max_length=100)
    fk_plano_contas = models.ForeignKey('PlanoContas', models.DO_NOTHING)
    fk_documento = models.ForeignKey(Documentos, models.DO_NOTHING)
    fk_fornecedor = models.ForeignKey(Fornecedores, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lancar_financeiro_viagens'


class LancarViagens(models.Model):
    id = models.BigAutoField(primary_key=True)
    crtc = models.CharField(max_length=30)
    data = models.DateField()
    fk_frota = models.ForeignKey(Frotas, models.DO_NOTHING)
    fk_motorista = models.ForeignKey(Funcionarios, models.DO_NOTHING)
    fk_origem_id = models.BigIntegerField()
    kmfinal = models.IntegerField(db_column='kmFinal')  # Field name made lowercase.
    kminicial = models.IntegerField(db_column='kmInicial')  # Field name made lowercase.
    litragem = models.FloatField()
    qtdeveiculos = models.IntegerField()
    fk_destino_id = models.BigIntegerField()
    fk_empresa = models.ForeignKey(Empresas, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lancar_viagens'


class Niveis(models.Model):
    nivel = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'niveis'


class PlanoContas(models.Model):
    id = models.BigAutoField(primary_key=True)
    conta = models.IntegerField()
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=20)
    subconta = models.IntegerField()
    sigla_situacao = models.CharField(max_length=1)
    saldo = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'plano_contas'


class Situacoes(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_nome = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'situacoes'


class TiposVeiculos(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo_de_veiculo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipos_veiculos'


class Usuarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=25)
    nivel = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'usuarios'


class Veiculos(models.Model):
    id = models.BigAutoField(primary_key=True)
    fk_tipo_veiculo = models.ForeignKey(TiposVeiculos, models.DO_NOTHING)
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    placas = models.CharField(max_length=80)
    datacompra = models.DateField(db_column='dataCompra')  # Field name made lowercase.
    fk_empresas = models.ForeignKey(Empresas, models.DO_NOTHING)
    fk_frota = models.ForeignKey(Frotas, models.DO_NOTHING)
    tipo_aquisicao = models.CharField(max_length=50)
    km_inicial = models.IntegerField()
    fk_situacoes = models.ForeignKey(Situacoes, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'veiculos'
