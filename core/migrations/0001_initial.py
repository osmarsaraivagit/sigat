# Generated by Django 4.2.16 on 2024-10-13 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cidades',
            },
        ),
        migrations.CreateModel(
            name='Destinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cidades')),
            ],
            options={
                'db_table': 'destinos',
            },
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_doc', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'documentos',
            },
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cnpj', models.CharField(db_column='CNPJ', max_length=80)),
                ('ie', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('endereco', models.CharField(max_length=100)),
                ('fone', models.CharField(max_length=30)),
                ('responsavel', models.CharField(max_length=80)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('fk_cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cidades')),
            ],
            options={
                'db_table': 'empresas',
            },
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'estados',
            },
        ),
        migrations.CreateModel(
            name='Exames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('cid', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'exames',
            },
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'forma_pagamento',
            },
        ),
        migrations.CreateModel(
            name='Fornecedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('cnpj', models.CharField(db_column='CNPJ', max_length=80)),
                ('ie', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('endereco', models.CharField(max_length=80)),
                ('fone', models.CharField(max_length=30)),
                ('responsavel', models.CharField(max_length=80)),
                ('data_cadastro', models.DateField(blank=True, null=True)),
                ('fk_cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cidades')),
                ('fk_estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estados')),
            ],
            options={
                'db_table': 'fornecedores',
            },
        ),
        migrations.CreateModel(
            name='Frotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_frota', models.CharField(max_length=20)),
                ('data_cadastro', models.DateField(blank=True, null=True)),
                ('fk_empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.empresas')),
            ],
            options={
                'db_table': 'frotas',
            },
        ),
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('cpf', models.CharField(db_column='CPF', max_length=50)),
                ('pis', models.CharField(db_column='PIS', max_length=30)),
                ('data_admissao', models.DateField(blank=True)),
                ('data_demissao', models.DateField(blank=True, null=True)),
                ('email', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=90)),
                ('telefone', models.CharField(max_length=60)),
                ('obs', models.CharField(max_length=100)),
                ('fk_cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cidades')),
                ('fk_estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estados')),
            ],
            options={
                'db_table': 'funcionarios',
            },
        ),
        migrations.CreateModel(
            name='Funcoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'funcoes',
            },
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'paises',
            },
        ),
        migrations.CreateModel(
            name='PlanoContas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conta', models.IntegerField()),
                ('tipo', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=20)),
                ('subconta', models.IntegerField()),
                ('sigla_situacao', models.CharField(max_length=1)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                'db_table': 'plano_contas',
            },
        ),
        migrations.CreateModel(
            name='Situacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_nome', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'situacoes',
            },
        ),
        migrations.CreateModel(
            name='TiposVeiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_veiculo', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tipos_veiculos',
            },
        ),
        migrations.CreateModel(
            name='Veiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=80)),
                ('modelo', models.CharField(max_length=80)),
                ('ano', models.IntegerField()),
                ('data_fabricacao', models.DateField(blank=True)),
                ('renavam', models.IntegerField()),
                ('placas', models.CharField(max_length=80)),
                ('datacompra', models.DateField(blank=True, verbose_name='data')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12)),
                ('tipo_aquisicao', models.CharField(max_length=50)),
                ('km_inicial', models.IntegerField()),
                ('obs', models.CharField(max_length=100)),
                ('fk_empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.empresas')),
                ('fk_frota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.frotas')),
                ('fk_situacoes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.situacoes')),
                ('fk_tipo_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tiposveiculos')),
            ],
            options={
                'db_table': 'veiculos',
            },
        ),
        migrations.CreateModel(
            name='Origens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cidades')),
                ('fk_estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estados')),
                ('fk_pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.paises')),
            ],
            options={
                'db_table': 'origens',
            },
        ),
        migrations.CreateModel(
            name='LancarViagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crtc', models.CharField(max_length=30)),
                ('data', models.DateField(blank=True)),
                ('kminicial', models.IntegerField(db_column='kmInicial')),
                ('litragem', models.FloatField()),
                ('qtdeveiculos', models.IntegerField()),
                ('obs', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=30)),
                ('fk_destino', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.destinos')),
                ('fk_empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.empresas')),
                ('fk_frota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.frotas')),
                ('fk_motorista', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.funcionarios')),
                ('fk_origem', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.origens')),
            ],
            options={
                'db_table': 'lancar_viagens',
            },
        ),
        migrations.CreateModel(
            name='LancarFinanceiroViagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12)),
                ('historico', models.CharField(max_length=100)),
                ('fk_documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.documentos')),
                ('fk_empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.empresas')),
                ('fk_fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.fornecedores')),
                ('fk_lancar_viagens', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.lancarviagens')),
                ('fk_plano_contas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.planocontas')),
            ],
            options={
                'db_table': 'lancar_financeiro_viagens',
            },
        ),
        migrations.CreateModel(
            name='LancarFerias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(blank=True)),
                ('data_fim', models.DateField(blank=True)),
                ('ano_referente', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12)),
                ('fk_funcionarios', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.funcionarios')),
            ],
            options={
                'db_table': 'lancar_ferias',
            },
        ),
        migrations.CreateModel(
            name='LancarDocVeiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('data_realizado', models.DateField(blank=True)),
                ('data_vencimento', models.DateField(blank=True)),
                ('obs', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=30)),
                ('fk_empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.empresas')),
                ('fk_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.veiculos')),
            ],
            options={
                'db_table': 'lancar_doc_veiculos',
            },
        ),
        migrations.CreateModel(
            name='LancarContabilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12)),
                ('historico', models.CharField(max_length=100)),
                ('fk_documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.documentos')),
                ('fk_empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.empresas')),
                ('fk_fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.fornecedores')),
                ('fk_plano_contas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.planocontas')),
                ('fk_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.veiculos')),
            ],
            options={
                'db_table': 'lancar_contabilidade',
            },
        ),
        migrations.CreateModel(
            name='LancarBaixaVeiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_venda', models.DateField(blank=True)),
                ('km_final', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12)),
                ('comprador', models.CharField(max_length=60)),
                ('telefone_comprador', models.CharField(max_length=40)),
                ('fk_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.veiculos')),
            ],
            options={
                'db_table': 'lancar_baixa_veiculos',
            },
        ),
        migrations.AddField(
            model_name='funcionarios',
            name='fk_situacoes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.situacoes'),
        ),
        migrations.AddField(
            model_name='funcionarios',
            name='funcao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.funcoes'),
        ),
        migrations.AddField(
            model_name='frotas',
            name='fk_situacoes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.situacoes'),
        ),
        migrations.AddField(
            model_name='empresas',
            name='fk_estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estados'),
        ),
        migrations.AddField(
            model_name='destinos',
            name='fk_estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estados'),
        ),
        migrations.AddField(
            model_name='destinos',
            name='fk_pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.paises'),
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('cnpj', models.CharField(db_column='CNPJ', max_length=60)),
                ('ie', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=80)),
                ('telefone', models.CharField(max_length=60)),
                ('data_cadastro', models.DateField(blank=True, null=True)),
                ('fk_cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cidades')),
                ('fk_estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estados')),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='AcertosViagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_acerto', models.DateField(blank=True)),
                ('km_final', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=11)),
                ('historico', models.CharField(max_length=100)),
                ('fk_forma_pagamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.formapagamento')),
                ('fk_lancar_viagens', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.lancarviagens')),
                ('fk_plano_contas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.planocontas')),
            ],
            options={
                'db_table': 'acertos_viagens',
            },
        ),
    ]
