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
			return HttpResponseRedirect("/listar_tema/")
	return render_to_response("temas.html",{"temas":fTemas()},RequestContext(request))

def pagina_pregunta(request):
	if request.method=="POST":
		form=fPreguntas(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect("/listar_pregunta/")
	return render_to_response("preguntas.html",{"preguntas":fPreguntas()},RequestContext(request))

def modificar_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	if request.method=="POST":
			formulario=fPreguntas(request.POST)
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect("/pregunta/perfil/{{pregunta.id}}/")
	else:
		formulario=fPreguntas(instance=pregunta)
	return render_to_response("modificar_pregunta.html",{"preguntas":fPreguntas()},RequestContext(request))

def eliminar_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	pregunta.delete()
	return HttpResponseRedirect("/listar_pregunta/")

def listar_pregunta(request):
	pregunta=Pregunta.objects.all()
	return render_to_response("listar_pregunta.html",{'pregunta':pregunta},context_instance=RequestContext(request))

def pregunta_ver(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	return render_to_response("pregunta_ver.html",{'pregunta':pregunta},context_instance=RequestContext(request))

def listar_tema(request):
	tema=Tema.objects.all()
	return render_to_response("listar_tema.html",{'tema':tema},context_instance=RequestContext(request))