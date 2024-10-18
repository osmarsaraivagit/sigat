from django.contrib import admin
from django.urls import path
from .views import home, lista_estados, estado_novo, estado_search, estado_update, estado_delete

urlpatterns = [

#url home, chama view home, cujo nome é 'home'
    path('home', home, name='home'),

#ESTADOS
    path('lista_estados', lista_estados, name='lista_estados'),
    path('estado_novo', estado_novo, name='estado_novo'),
    path('estado_update/<int:id>', estado_update, name='estado_update'),
    path('estado_delete/<int:id>', estado_delete, name='estado_delete'),
    path('estado_search', estado_search, name='estado_search')

]















































































































