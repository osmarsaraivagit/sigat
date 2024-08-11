from django.contrib import admin
from django.urls import path
from .views import home, lista_localidades, localidade_novo, localidade_update, localidade_search, localidade_delete
from .views import lista_empresas, empresa_novo, empresa_update, empresa_search, empresa_delete

urlpatterns = [
    
    #localidades
    path('home', home, name='home'), #url home, chama view home, cujo nome é 'home'
    path('lista_localidades', lista_localidades, name='lista_localidades'),
    path('localidade_novo', localidade_novo, name='localidade_novo'),
    path('localidade_update/<int:id>', localidade_update, name='localidade_update'),
    path('localidade_search', localidade_search, name='localidade_search'),
    #path('delete/<int:pk>', LocalidadeDeleteView.as_view(), name='localidade_delete'),
    #path('localidades_confirm_delete', localidades_confirm_delete, name='localidades_confirm_delete'), 
    path('localidade_delete/<int:id>', localidade_delete, name='localidade_delete'),
    
    #empresas
    path('lista_empresas', lista_empresas, name='lista_empresas'),
    path('empresa_novo', empresa_novo, name='empresa_novo'),
    path('empresa_update/<int:id>', empresa_update, name='empresa_update'),
    path('empresa_search', empresa_search, name='empresa_search'),
    path('empreesa_delete/<int:id>', empresa_delete, name='empresa_delete'),
    
    
]















































































































