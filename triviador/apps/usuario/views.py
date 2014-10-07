from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# Create your views here.

def registro_view(request):
	if request.method=="POST":
		formulario_registro=fusuario(request.POST)
		if formulario_registro.is_valid():
			nuevo_usuario=request.POST['username']
			formulario_registro.save()
			usuario=User.objects.get(username=nuevo_usuario)
			usuario.is_active=False
			usuario.save()
			perfil=Perfil.objects.create(user=usuario)
			return HttpResponseRedirect("/login/")
	else:
		formulario_registro=fusuario()
	return render_to_response("registro_user.html",{'formulario':formulario_registro},context_instance=RequestContext(request))

def login_view(request):
	if request.method=="POST":
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario=request.POST['username']
			contrasena=request.POST['password']
			acceso=authenticate(username=usuario, password=contrasena)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect("/user/perfil")
				else:
					login(request, acceso)
					return HttpResponseRedirect("/user/active")
		else:
			return HttpResponse("Error en los datos")
	else:
		formulario=AuthenticationForm()
	return render_to_response("loginn.html", {"formulario":formulario}, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

def perfil_view(request):
	return render_to_response("perfil_u.html",{},context_instance=RequestContext(request))

def user_active_view(request):
	if request.user.is_authenticated():
		usuario=request.user
		if usuario.is_active:
			return HttpResponseRedirect("/user/perfil/")
		else:
			if request.method=="POST":
				u=User.objects.get(username=usuario)
				perfil=Perfil.objects.get(user=u)
				formulario=fperfil(request.POST,request.FILES,instance=perfil)
				if formulario.is_valid():
					formulario.save()
					u.is_active=True
					u.save()
					return HttpResponseRedirect("/user/perfil/")
			else:
				formulario=fperfil()
			return render_to_response("activar.html", {"formulario":formulario}, context_instance=RequestContext(request))
	else:
			return HttpResponseRedirect("/login/")

def modificar_perfil(request):
	if request.user.is_authenticated():
		u=request.user
		usuario=User.objects.get(username=u)
		perfil=Perfil.objects.get(user=usuario)
		if request.method=='POST':
			formulario=fperfil_modificar(request.POST,request.FILES,instance=perfil)
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect("/user/perfil/")
		else:
			formulario=fperfil_modificar(instance=perfil)
			return render_to_response('modificar_perfil.html',{'formulario':formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")


def jugar_view(request):
	return render_to_response("calendar.html", context_instance=RequestContext(request))

def listar_usuario(request):
	u=request.user
	usuario=User.objects.all()
	return render_to_response("listar_usuarios.html",{'usuarios':usuario},context_instance=RequestContext(request))

def registro_admin(request):
	if request.method=="POST":
		formulario_r=fadmin(request.POST)
		if formulario_r.is_valid():
			usuario=request.POST['username']
			formulario_r.save()
			anio=request.POST['fecha_nacimiento_year']
			mes=request.POST['fecha_nacimiento_month']
			dia=request.POST['fecha_nacimiento_day']
			fecha_nacimiento=anio+"_"+mes+"_"+dia
			imagen=request.FILES['imagen']
			sexo=request.POST['sexo']
			ci=request.POST['si']
			telefono=request.POST['telefono']
			usuario_nuevo=User.objects.get(username=usuario)
			usuario_nuevo.is_active=False
			usuario_nuevo.save()
			perfil=Perfil.objects.create(user=usuario_nuevo,fecha_nacimiento=fecha_nacimiento,imagen=imagen,sexo=sexo,ci=ci,telefono=telefono)
			return HttpResponseRedirect("/login/")
	else:
		formulario_r=fadmin()
	return render_to_response("registro_user.html",{'formulario':formulario_re},context_instance=RequestContext(request))