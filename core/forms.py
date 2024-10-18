from django.forms import ModelForm
from .models import Origem, Destino, Empresa, Fornecedor, Cliente, Documento, Frota, Funcionario, PlanoConta
from .models import Situacao, AcertoViagem, TipoVeiculo, Veiculo, LancarViagem, LancarFinanceiroViagem
from .models import LancarFerias, LancarContabilidade, LancarBaixaVeiculo, Estado, Cidade, Pais


class EstadoForm(ModelForm):
    class Meta:
        model = Estado
        fields = '__all__'

class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'


class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

class OrigemForm(ModelForm):
    class Meta:
        model = Origem
        fields = '__all__'

class DestinoForm(ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class DocumentoForm(ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'

class FrotaForm(ModelForm):
    class Meta:
        model = Frota
        fields = '__all__'

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

class PlanoContasForm(ModelForm):
    class Meta:
        model = PlanoConta
        fields = '__all__'

class SituacaoForm(ModelForm):
    class Meta:
        model = Situacao
        fields = '__all__'

class AcertoViagemForm(ModelForm):
    class Meta:
        model = AcertoViagem
        fields = '__all__'

class TipoVeiculoForm(ModelForm):
    class Meta:
        model = TipoVeiculo
        fields = '__all__'

class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

class lancarViagemForm(ModelForm):
    class Meta:
        model = LancarViagem
        fields = '__all__'

class LancarFinanceiroViagemForm(ModelForm):
    class Meta:
        model = LancarFinanceiroViagem
        fields = '__all__'

class LancarFeriasForm(ModelForm):
    class Meta:
        model = LancarFerias
        fields = '__all__'

class LancarContabilidadeForm(ModelForm):
    class Meta:
        model = LancarContabilidade
        fields = '__all__'

class LancarBaixaVeiculoForm(ModelForm):
    class Meta:
        model = LancarBaixaVeiculo
        fields = '__all__'

