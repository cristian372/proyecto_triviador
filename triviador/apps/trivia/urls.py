from django.conf.urls import patterns, include, url
from .views import *
from django.contrib import admin
urlpatterns = patterns('',
    url(r'^$', indice, name='Inicio'),
)
