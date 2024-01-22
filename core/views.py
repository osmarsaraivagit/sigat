from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from .models import Localidades
from .forms import LocalidadesForm
from .models import Empresas
from .forms import EmpresasForm

def home(request):
    return render(request, 'home.html')
  
def localidades_confirm_delete(request):
    return render(request, 'core/localidades_confirm_delete.html')


def lista_localidades(request):
    form = LocalidadesForm
    localidades_list = Localidades.objects.all().order_by('cidade')
    paginator = Paginator(localidades_list, 5)
    page = request.GET.get('page')
    localidades = paginator.get_page(page)
    data = {}
    data['localidades'] = localidades
    data['form'] = form
    return render(request, 'core/lista_localidades.html', data)


def localidade_novo(request):
    if request.method == "POST":
        cidade = request.POST.get('cidade') 
        estado = request.POST.get('estado') 
        count_1= Localidades.objects.filter(cidade=cidade).count()
        count_2= Localidades.objects.filter(estado=estado).count()
        if count_1 and count_2 > 0:
                messages.error(request, "Registro já cadastrado com estes mesmos nomes!")
                return redirect('localidade_novo')
        else:
            form = LocalidadesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_localidades')
    else:
        form = LocalidadesForm
        return render(request, 'core/localidade_novo.html', {'form':form})
    
    
def localidade_update(request, id):
    localidade = Localidades.objects.get(id=id)
    form = LocalidadesForm(request.POST or None, instance=localidade)
    data={}
    data['localidade'] = localidade
    data['form'] = form
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Registro atualizado com Sucesso!")
            return redirect('lista_localidades')
    else:
        form = LocalidadesForm
        return render(request, 'core/localidade_update.html', data)
    
    
def localidade_search(request):
        search = request.GET.get('search')
        localidade = Localidades.objects.filter(cidade__icontains=search)
        form = LocalidadesForm()
        data = {}
        data['localidades'] = localidade
        data['form'] = form
        return render (request, 'core/lista_localidades.html', data)
    
     
def localidade_delete(request, id):
    localidade = Localidades.objects.get(id=id)
    localidade.delete()
    messages.success(request, "Registro Excluído com Sucesso!")
    return redirect('lista_localidades')

#empresas
######################################################################

def lista_empresas(request):
    form = EmpresasForm
    empresas_list= Empresas.objects.all().order_by('nome')
    paginator = Paginator(empresas_list, 5)
    page = request.GET.get('page')
    empresas = paginator.get_page(page)
    data = {}
    data['empresas'] = empresas
    data['form'] = form
    return render(request, 'core/lista_empresas.html', data)


def empresas_confirm_delete(request):
    return render(request, 'core/empresas_confirm_delete.html')


def empresa_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome') 
        cnpj = request.POST.get('cnpj') 
        count_1= empresas.objects.filter(nome=nome).count()
        count_2= empresas.objects.filter(cnpje=cnpj).count()
        if count_1 and count_2 > 0:
                messages.error(request, "Registro já cadastrado com estes mesmos nomes!")
                return redirect('empresa_novo')
        else:
            form = EmpresasForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_empresas')
    else:
        form = EmpresasForm
        return render(request, 'core/empresa_novo.html', {'form':form})
    
    
def empresa_update(request, id):
    localidade = Empresas.objects.get(id=id)
    form = EmpresasForm(request.POST or None, instance=empresa)
    data={}
    data['empresa'] = empresa
    data['form'] = form
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Registro atualizado com Sucesso!")
            return redirect('lista_empresas')
    else:
        form = EmpresasForm
        return render(request, 'core/empresa_update.html', data)
    
    
def empresa_search(request):
        search = request.GET.get('search')
        empresa = Empresas.objects.filter(nome__icontains=search)
        form = EmpresasForm()
        data = {}
        data['empresas'] = empresa
        data['form'] = form
        return render (request, 'core/lista_empresas.html', data)
    
     
def empresa_delete(request, id):
    empresa = Empresas.objects.get(id=id)
    empresa.delete()
    messages.success(request, "Registro Excluído com Sucesso!")
    return redirect('lista_empresas')
