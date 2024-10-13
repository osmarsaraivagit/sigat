from django.contrib import admin
from django.urls import path

from .views import home
#from .views import lista_empresas, empresa_novo, empresa_update, empresa_search, empresa_delete

urlpatterns = [
    

    path('home', home, name='home') #url home, chama view home, cujo nome é 'home'

    #path('lista_origens', lista_origens, name='lista_origens'),
    #path('origens_novo', origens_novo, name='origens_novo'),
    #path('origens_update/<int:id>', origens_update, name='origens_update'),
    #path('origens_search', origens_search, name='origens_search'),
    #path('origens_delete/<int:id>', origens_delete, name='origens_delete'),
    
    #empresas
    #path('lista_empresas', lista_empresas, name='lista_empresas'),
    #path('empresa_novo', empresa_novo, name='empresa_novo'),
    #path('empresa_update/<int:id>', empresa_update, name='empresa_update'),
    #path('empresa_search', empresa_search, name='empresa_search'),
    #path('empreesa_delete/<int:id>', empresa_delete, name='empresa_delete'),
    
    
]















































































































