from django.conf.urls import patterns, include, url
from .views import *
from django.contrib import admin
urlpatterns = patterns('',
    url(r'^$', indice, name='Inicio'),
    url(r'^tema/$', pagina_tema),
    url(r'^pregunta/$', pagina_pregunta),
    url(r'^perfil/modificar/(\d+)/$',modificar_pregunta),
    url(r'^perfil/eliminar/(\d+)/$',eliminar_pregunta),
    url(r'^listar_pregunta/$',listar_pregunta),
    url(r'^pregunta/perfil/(\d+)/$',pregunta_ver),
)
