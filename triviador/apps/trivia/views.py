from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

# Create your views here.

def indice(request):
	return render_to_response("index.html", RequestContext(request))

def pagina_tema(request):
	if request.method=="POST":
		form=fTemas(request.POST)
		if(form.is_valid()):
			form.save()
	return render_to_response("temas.html",{"temas":fTemas()},RequestContext(request))

def pagina_pregunta(request):
	if request.method=="POST":
		form=fPreguntas(request.POST)
		if(form.is_valid()):
			form.save()
	return render_to_response("preguntas.html",{"preguntas":fPreguntas()},RequestContext(request))