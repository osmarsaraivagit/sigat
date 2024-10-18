from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from .models import Estado, Cidade
from .forms import EstadoForm, CidadeForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

#ESTADOS
def lista_estados(request):
    form = EstadoForm
    estados_list = Estado.objects.all().order_by('nome')
    paginator = Paginator(estados_list, 5)
    page = request.GET.get('page')
    estado = paginator.get_page(page)
    data = {}
    data['estado'] = estado
    data['form'] = form
    return render(request, 'core/lista_estados.html', data)

def estado_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Estado.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, "Registro já cadastrao com este Nome!")
            return redirect('estado_novo')
        else:
            form = EstadoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_estados')
    else:
        form = EstadoForm
        return render(request, 'core/estado_novo.html', {'form': form})

def estado_update(request, id):
        estado = Estado.objects.get(id=id)
        form = EstadoForm(request.POST or None, instance=estado)
        data = {}
        data['estado'] = estado
        data['form'] = form
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('lista_estados')
        else:
            form = EstadoForm
        return render(request, 'core/estado_update.html', data)

def estado_delete(request, id):
    estado = Estado.objects.get(id=id)
    estado.delete()
    messages.success(request, "Registro Excluído com Sucesso!")
    return redirect('lista_estados')

def estado_search(request):
    search = request.GET.get('search')
    estado = Estado.objects.filter(nome__icontains=search)
    form = EstadoForm()
    data = {}
    data['estado'] = estado
    data['form'] = form
    return render(request, 'core/lista_estados.html', data)


###################################################################

#CIDADES

def lista_cidades(request):
    form = CidadeForm
    cidades_list = Cidade.objects.all().order_by('nome')
    paginator = Paginator(cidades_list, 5)
    page = request.GET.get('page')
    cidade = paginator.get_page(page)
    data = {}
    data['cidade'] = cidade
    data['form'] = form
    return render(request, 'core/lista_cidades.html', data)

def cidade_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Cidade.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, "Registro já cadastrao com este Nome!")
            return redirect('cidade_novo')
        else:
            form = CidadeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_cidades')
    else:
        form = CidadeForm
        return render(request, 'core/cidade_novo.html', {'form': form})

def cidade_update(request, id):
        cidade = Cidade.objects.get(id=id)
        form = CidadeForm(request.POST or None, instance=cidade)
        data = {}
        data['cidade'] = cidade
        data['form'] = form
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('lista_cidades')
        else:
            form = CidadeForm
        return render(request, 'core/cidade_update.html', data)

def cidade_delete(request, id):
    cidade = Cidade.objects.get(id=id)
    cidade.delete()
    messages.success(request, "Registro Excluído com Sucesso!")
    return redirect('lista_cidades')

def cidade_search(request):
    search = request.GET.get('search')
    cidade = Cidade.objects.filter(nome__icontains=search)
    form = CidadeForm()
    data = {}
    data['cidade'] = cidade
    data['form'] = form
    return render(request, 'core/lista_cidades.html', data)

####################################################################