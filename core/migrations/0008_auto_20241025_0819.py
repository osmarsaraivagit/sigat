# Generated by Django 3.1.5 on 2024-10-25 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20241024_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acertoviagem',
            old_name='fk_forma_pagamento',
            new_name='forma_pagamento',
        ),
        migrations.RenameField(
            model_name='acertoviagem',
            old_name='fk_lancar_viagem',
            new_name='lancar_viagem',
        ),
        migrations.RenameField(
            model_name='acertoviagem',
            old_name='fk_plano_conta',
            new_name='plano_conta',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='fk_cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='fk_estado',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='destino',
            old_name='fk_cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='destino',
            old_name='fk_estado',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='destino',
            old_name='fk_pais',
            new_name='pais',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='fk_cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='fk_estado',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='fornecedor',
            old_name='fk_cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='fornecedor',
            old_name='fk_estado',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='frota',
            old_name='fk_empresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='frota',
            old_name='fk_situacoes',
            new_name='situacoes',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='fk_cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='fk_estado',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='fk_funcao',
            new_name='funcao',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='fk_situacoes',
            new_name='situacoes',
        ),
        migrations.RenameField(
            model_name='lancarbaixaveiculo',
            old_name='fk_veiculo',
            new_name='veiculo',
        ),
        migrations.RenameField(
            model_name='lancarcontabilidade',
            old_name='fk_documento',
            new_name='documento',
        ),
        migrations.RenameField(
            model_name='lancarcontabilidade',
            old_name='fk_empresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='lancarcontabilidade',
            old_name='fk_fornecedor',
            new_name='fornecedor',
        ),
        migrations.RenameField(
            model_name='lancarcontabilidade',
            old_name='fk_plano_conta',
            new_name='plano_conta',
        ),
        migrations.RenameField(
            model_name='lancarcontabilidade',
            old_name='fk_veiculo',
            new_name='veiculo',
        ),
        migrations.RenameField(
            model_name='lancardocveiculo',
            old_name='fk_empresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='lancardocveiculo',
            old_name='fk_veiculo',
            new_name='veiculo',
        ),
        migrations.RenameField(
            model_name='lancarferias',
            old_name='fk_funcionario',
            new_name='funcionario',
        ),
        migrations.RenameField(
            model_name='lancarfinanceiroviagem',
            old_name='fk_documento',
            new_name='documento',
        ),
        migrations.RenameField(
            model_name='lancarfinanceiroviagem',
            old_name='fk_empresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='lancarfinanceiroviagem',
            old_name='fk_fornecedor',
            new_name='fornecedor',
        ),
        migrations.RenameField(
            model_name='lancarfinanceiroviagem',
            old_name='fk_lancar_viagem',
            new_name='lancar_viagem',
        ),
        migrations.RenameField(
            model_name='lancarfinanceiroviagem',
            old_name='fk_plano_conta',
            new_name='plano_conta',
        ),
        migrations.RenameField(
            model_name='lancarviagem',
            old_name='fk_destino',
            new_name='destino',
        ),
        migrations.RenameField(
            model_name='lancarviagem',
            old_name='fk_frota',
            new_name='frota',
        ),
        migrations.RenameField(
            model_name='lancarviagem',
            old_name='fk_motorista',
            new_name='motorista',
        ),
        migrations.RenameField(
            model_name='lancarviagem',
            old_name='fk_origem',
            new_name='origem',
        ),
        migrations.RenameField(
            model_name='veiculo',
            old_name='fk_empresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='veiculo',
            old_name='fk_frota',
            new_name='frota',
        ),
        migrations.RenameField(
            model_name='veiculo',
            old_name='fk_situacoes',
            new_name='situacoes',
        ),
        migrations.RenameField(
            model_name='veiculo',
            old_name='fk_tipo_veiculo',
            new_name='tipo_veiculo',
        ),
    ]
