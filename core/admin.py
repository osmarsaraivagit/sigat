from django.contrib import admin

from .models import Localidades, Empresas, Fornecedores, Clientes, Documentos, Frotas, Funcionarios, PlanoContas
from .models import Situacoes, AcertosViagens, TiposVeiculos, Veiculos, LancarViagens, LancarFinanceiroViagens
from .models import LancarFerias, LancarContabilidade, LancarBaixaVeiculos

admin.site.register(Localidades)
admin.site.register(Empresas)
admin.site.register(Fornecedores)
admin.site.register(Clientes)
admin.site.register(Documentos)
admin.site.register(Frotas)
admin.site.register(Funcionarios)
admin.site.register(PlanoContas)
admin.site.register(Situacoes)
admin.site.register(AcertosViagens)
admin.site.register(TiposVeiculos)
admin.site.register(Veiculos)
admin.site.register(LancarViagens)
admin.site.register(LancarFinanceiroViagens)
admin.site.register(LancarFerias)
admin.site.register(LancarContabilidade)
admin.site.register(LancarBaixaVeiculos)


