from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request, 'home.html')