from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from .models import Estado
from .forms import EstadoForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

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