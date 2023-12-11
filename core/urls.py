from django.contrib import admin
from django.urls import path
from .views import home, lista_localidades, localidade_novo, localidade_update


urlpatterns = [
    path('home', home, name='home'), #url home, chama view home, cujo nome é 'home'
    path('lista_localidades', lista_localidades, name='lista_localidades'),
    path('localidade_novo', localidade_novo, name='localidade_novo'),
    path('localidade_update/<int:id>', localidade_update, name='localidade_update'),
]
