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
		formulario=ftema(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/listar_tema/")
	return render_to_response("temas.html",{"temas":ftema()},RequestContext(request))

def pagina_pregunta(request):
	if request.method=="POST":
		formulario=fpregunta(request.POST)
		formulario2=frespuesta(request.POST)
		if formulario.is_valid() and formulario2.is_valid():
			pregunta=formulario.save(commit=False)
			pregunta.tema=Tema
			pregunta.save()
			respuesta=formulario2.save(commit=False)
			respuesta.pregunta=pregunta
			respuesta.save()
			formulario=fpregunta()
			return HttpResponseRedirect("/listar_pregunta/")
	else:
		formulario=fpregunta()
		formulario2=frespuesta()
	datos={'formulario':formulario,'formulario2':formulario2}
	return render_to_response("preguntas.html",datos,context_instance=RequestContext(request))

def modificar_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	respuesta=Respuesta.objects.get(pregunta=pregunta)
	if request.method=="POST":
		formulario=fpregunta(request.POST,instance=pregunta)
		formulario2=frespuesta(request.POST,instance=respuesta)
		if formulario.is_valid() and formulario2.is_valid():
			formulario.save()
			formulario2.save()
			datos={'formulario':formulario,'formulario2':formulario2}
			return render_to_response("modificar_pregunta.html",datos,context_instance=RequestContext(request))
	else:
		formulario=fpregunta(instance=pregunta)
		formulario2=frespuesta(instance=respuesta)
	datos={'formulario':formulario,'formulario2':formulario2}
	return render_to_response("modificar_pregunta.html",datos,context_instance=RequestContext(request))

def eliminar_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	id=pregunta.Tema.id
	respuesta=Respuesta.objects.get(pregunta=pregunta)
	pregunta.delete()
	respuesta.delete()
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