from django.contrib import admin
from django.urls import path
from .views import home, lista_localidades


urlpatterns = [
    path('home', home, name='home'), #url home, chama view home, cujo nome é 'home'
    path('lista_localidades', lista_localidades, name='lista_localidades'),
]
