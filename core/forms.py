from django.forms import ModelForm
from .models import Localidades, Empresas, Fornecedores, Clientes, Documentos, Frotas, Funcionarios, PlanoContas
from .models import Situacoes, AcertosViagens, TiposVeiculos, Veiculos, LancarViagens, LancarFinanceiroViagens
from .models import LancarFerias, LancarContabilidade, LancarBaixaVeiculos

class LocalidadesForm(ModelForm):
    class Meta:
        model = Localidades
        fields = '__all__'

class EmpresasForm(ModelForm):
    class Meta:
        model = Empresas
        fields = '__all__'

class FornecedoresForm(ModelForm):
    class Meta:
        model = Fornecedores
        fields = '__all__'

class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'

class DocumentosForm(ModelForm):
    class Meta:
        model = Documentos
        fields = '__all__'

class FrotasForm(ModelForm):
    class Meta:
        model = Frotas
        fields = '__all__'

class FuncionariosForm(ModelForm):
    class Meta:
        model = Funcionarios
        fields = '__all__'

class PlanoContasForm(ModelForm):
    class Meta:
        model = PlanoContas
        fields = '__all__'

class SituacoesForm(ModelForm):
    class Meta:
        model = Situacoes
        fields = '__all__'

class AcertosViagensForm(ModelForm):
    class Meta:
        model = AcertosViagens
        fields = '__all__'

class TiposVeiculosForm(ModelForm):
    class Meta:
        model = TiposVeiculos
        fields = '__all__'

class VeiculosForm(ModelForm):
    class Meta:
        model = Veiculos
        fields = '__all__'

class lancarViagensForm(ModelForm):
    class Meta:
        model = LancarViagens
        fields = '__all__'

class LancarFinanceiroViagensForm(ModelForm):
    class Meta:
        model = LancarFinanceiroViagens
        fields = '__all__'

class LancarFeriasForm(ModelForm):
    class Meta:
        model = LancarFerias
        fields = '__all__'

class LancarContabilidadeForm(ModelForm):
    class Meta:
        model = LancarContabilidade
        fields = '__all__'

class LancarBaixaVeiculosForm(ModelForm):
    class Meta:
        model = LancarBaixaVeiculos
        fields = '__all__'

