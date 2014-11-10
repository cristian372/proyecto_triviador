from django.conf.urls import patterns, include, url
from .views import *
from django.contrib import admin
urlpatterns = patterns('',
    url(r'^$', indice, name='Inicio'),
    url(r'^tema/$', pagina_tema),
    url(r'^pregunta/$', pagina_pregunta),
)
