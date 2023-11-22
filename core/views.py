from django.shortcuts import render, redirect
from .models import Localidades
from .forms import LocalidadesForm



def home(request):
    return render(request, 'core/home.html')

def lista_localidades(request):
    form = LocalidadesForm
    localidades = Localidades.objects.all().order_by('nome')

