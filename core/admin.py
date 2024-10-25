from django.contrib import admin

from .models import Estado, Cidade, Pais, Origem, Destino, Empresa, Fornecedor, Cliente, Documento, Frota, Funcionario, PlanoConta
from .models import Situacao, AcertoViagem, TipoVeiculo, Veiculo, LancarViagem, LancarFinanceiroViagem
from .models import LancarFerias, LancarContabilidade, LancarBaixaVeiculo, Funcao

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Pais)
admin.site.register(Origem)
admin.site.register(Destino)
admin.site.register(Funcao)
admin.site.register(Empresa)
admin.site.register(Fornecedor)
admin.site.register(Cliente)
admin.site.register(Documento)
admin.site.register(Frota)
admin.site.register(Funcionario)
admin.site.register(PlanoConta)
admin.site.register(Situacao)
admin.site.register(AcertoViagem)
admin.site.register(TipoVeiculo)
admin.site.register(Veiculo)
admin.site.register(LancarViagem)
admin.site.register(LancarFinanceiroViagem)
admin.site.register(LancarFerias)
admin.site.register(LancarContabilidade)
admin.site.register(LancarBaixaVeiculo)


