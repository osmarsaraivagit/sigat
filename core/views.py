from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Localidades
from .forms import LocalidadesForm



def home(request):
    return render(request, 'core/home.html')

def lista_localidades(request):
    form = LocalidadesForm
    localidades = Localidades.objects.all().order_by('cidade')
    return render(request, 'core/lista_localidades.html', {'form': form, 'localidades': localidades})

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
            return redirect('lista_localidades')
    else:
        form = LocalidadesForm
        return render(request, 'core/localidade_update.html', data)