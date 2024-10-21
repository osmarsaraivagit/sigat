from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from .models import Estado, Cidade, Pais, Origem
from .forms import EstadoForm, CidadeForm, PaisForm, OrigemForm


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


#PAISES

def lista_paises(request):
    form = PaisForm
    paises_list = Pais.objects.all().order_by('nome')
    paginator = Paginator(paises_list, 5)
    page = request.GET.get('page')
    pais = paginator.get_page(page)
    data = {}
    data['pais'] = pais
    data['form'] = form
    return render(request, 'core/lista_paises.html', data)

def pais_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Pais.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, "Registro já cadastrao com este Nome!")
            return redirect('pais_novo')
        else:
            form = PaisForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_paises')
    else:
        form = CidadeForm
        return render(request, 'core/pais_novo.html', {'form': form})

def pais_update(request, id):
        pais = Pais.objects.get(id=id)
        form = PaisForm(request.POST or None, instance=pais)
        data = {}
        data['pais'] = pais
        data['form'] = form
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('lista_paises')
        else:
            form = PaisForm
        return render(request, 'core/pais_update.html', data)

def pais_delete(request, id):
    pais = Pais.objects.get(id=id)
    pais.delete()
    messages.success(request, "Registro Excluído com Sucesso!")
    return redirect('lista_paises')

def pais_search(request):
    search = request.GET.get('search')
    pais = Pais.objects.filter(nome__icontains=search)
    form = PaisForm()
    data = {}
    data['pais'] = pais
    data['form'] = form
    return render(request, 'core/lista_paises.html', data)

####################################################################

#ORIGENS

def lista_origens(request):
    origens_list = Origem.objects.all().order_by('cidade_id')
    paginator = Paginator(origens_list,5)
    page = request.GET.get('page')
    origens = paginator.get_page(page)
    form = OrigemForm
    return render(request, 'core/lista_origens.html', {'origens': origens, 'form': form})

def origem_novo(request):
    if request.method == "POST":
        cidade_id = request.POST.get('cidade_id')
        estado_id = request.POST.get('estado_id')
        pais_id = request.POST.get('pais_id')
        o = Origem.objects.create(
            cidade_id = cidade_id,
            estado_id = estado_id,
            pais_id = pais_id
        )
        messages.success(request, 'Registro Cadastrado com Sucesso!')
        return redirect('lista_origens')

    else:
        form = OrigemForm()
        cidades = Cidade.objects.all().order_by('nome')
        estados = Estado.objects.all().order_by('nome')
        paises = Pais.objects.all().order_by('nome')
        return render(request, 'core/origem_novo.html',
        {
            'form': form,
            'cidades': cidades,
            'estados': estados,
            'paises': paises
        })

def origem_update(request, id):
    origem = Origem.objects.get(id=id)
    cidade_id = origem.cidade_id
    estado_id = origem.estado_id
    pais_id = origem.pais_id
    cidades = Cidade.objects.all().order_by('nome')
    estados = Estado.objects.all().order_by('nome')
    paises = Pais.objects.all().order_by('nome')
    data = {}
    data['origem'] = origem
    data['cidades'] = cidades
    data['estados'] = estados
    data['paises'] = paises
    if request.method == "POST":
        origem.cidade_id = request.POST.get('cidade_id')
        origem.estado_id = request.POST.get('estado_id')
        origem.pais_id = request.POST.get('pais_id')
        origem.save()
        messages.success(request, 'Registro Alterado com Sucesso !')
        return redirect('lista_origens')
    else:
        return render(request, 'core/origem_update.html', data)


def origem_delete(request, id):
    origem = Origem.objects.get(id=id)
    origem.delete()
    origens = Origem.objects.all().order_by('cidade_id')
    messages.success(request, 'Origem excluída com sucesso !')
    return render(request, 'core/lista_origens.html', {'origens': origens})


def origem_search(request):
    search = request.GET.get('search')
    origem = Origem.objects.filter(cidade_id=2)
    form = OrigemForm()
    data = {}
    data['origem'] = origem
    data['form'] = form
    return render(request, 'core/lista_origens.html')

