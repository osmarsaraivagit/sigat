from django.contrib import admin
from django.urls import path
from .views import home, lista_estados, estado_novo, estado_search, estado_update, estado_delete
from .views import lista_cidades, cidade_novo, cidade_search, cidade_update, cidade_delete
from .views import lista_paises, pais_novo, pais_search, pais_update, pais_delete
from .views import lista_origens, origem_novo, origem_update, origem_delete
from .views import lista_destinos, destino_novo, destino_delete, destino_update

urlpatterns = [

#url home, chama view home, cujo nome é 'home'
    path('home', home, name='home'),

#ESTADOS
    path('lista_estados', lista_estados, name='lista_estados'),
    path('estado_novo', estado_novo, name='estado_novo'),
    path('estado_update/<int:id>', estado_update, name='estado_update'),
    path('estado_delete/<int:id>', estado_delete, name='estado_delete'),
    path('estado_search', estado_search, name='estado_search'),



#CIDADES
    path('lista_cidades', lista_cidades, name='lista_cidades'),
    path('cidade_novo', cidade_novo, name='cidade_novo'),
    path('cidade_update/<int:id>', cidade_update, name='cidade_update'),
    path('cidade_delete/<int:id>', cidade_delete, name='cidade_delete'),
    path('cidade_search', cidade_search, name='cidade_search'),



#PAISES
    path('lista_paises', lista_paises, name='lista_paises'),
    path('pais_novo', pais_novo, name='pais_novo'),
    path('pais_update/<int:id>', pais_update, name='pais_update'),
    path('pais_delete/<int:id>', pais_delete, name='pais_delete'),
    path('pais_search', pais_search, name='pais_search'),


#ORIGEM
    path('lista_origens', lista_origens, name='lista_origens'),
    path('origem_novo', origem_novo, name='origem_novo'),
    path('origem_update/<int:id>', origem_update, name='origem_update'),
    path('origem_delete/<int:id>', origem_delete, name='origem_delete'),

#DESTINOS
    path('lista_destinos', lista_destinos, name='lista_destinos'),
    path('destino_novo', destino_novo, name='destino_novo'),
    path('destino_update/<int:id>', destino_update, name='destino_update'),
    path('destino_delete/<int:id>', destino_delete, name='destino_delete'),

]















































































































