from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
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
		if request.session['cont']>2:
			formulario2=fcaptcha(request.POST)
			if formulario2.is_valid():
				pass
			else:
				datos={'formulario':formulario,'formulario2':formulario2}
				return render_to_response("loginn.html",datos,context_instance=RequestContext(request))
		if formulario.is_valid:
			usuario=request.POST["username"]
			contrasena=request.POST["password"]
			acceso=authenticate(username=usuario, password=contrasena)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					p=SessionStore()
					p["name"]=usuario
					p["estado"]="conectado"
					p.save()
					request.session["idkey"]=p.session_key
					request.session["name"]=usuario
					request.session['cont'] = 0
					return HttpResponseRedirect("/user/perfil")
				else:
					login(request, acceso)
					return HttpResponseRedirect("/user/active")
			else:
				usuario=request.POST['username']
				if request.session['nombre_usuario']==usuario:
					request.session['cont']=request.session['cont']+1
				else:
					request.session['cont']=0
				request.session['nombre_usuario']=usuario
				aux=request.session['cont']				
				estado=True
				mensaje="Error en los datos "+str(usuario)
				if aux>3:
					formulario2=fcaptcha()
					datos={'formulario':formulario,'formulario2':formulario2,'estado':estado,'mensaje':mensaje}
				else:
					datos={'formulario':formulario,'estado':estado,'mensaje':mensaje}
				return render_to_response("loginn.html",datos,context_instance=RequestContext(request))
	else:
		request.session['nombre_usuario']=""
		request.session['cont']=0
		formulario=AuthenticationForm()
	return render_to_response("loginn.html", {"formulario":formulario}, context_instance=RequestContext(request))

def jugar(request):
	idsession=request.session['idkey']
	return HttpResponseRedirect("http://localhost:3002/juegos/"+idsession)

def logout_view(request):
	p=SessionStore(session_key=request.session['idkey'])
	p["estado"]="deconectado"
	p["name"]=""
	p.save()
	logout(request)
	return HttpResponseRedirect("/")

def perfil_view(request):
	return render_to_response("perfil_u.html",{},context_instance=RequestContext(request))

def perfil_ver(request,id):
	usuario=User.objects.get(id=int(id))
	return render_to_response("perfil_ver.html",{'usuario':usuario},context_instance=RequestContext(request))

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


#def jugar_view(request):
#	return render_to_response("calendar.html", context_instance=RequestContext(request))

def listar_usuario(request):
	usuarios=User.objects.all()
	return render_to_response("listar_usuarios.html",{'usuarios':usuarios},context_instance=RequestContext(request))

def registro_admin(request):
	if request.method=='POST':
		formulario=UserCreationForm(request.POST)
		formulario2=fadmin(request.POST,request.FILES)
		if formulario.is_valid() and formulario2.is_valid():
			usuario=request.POST['username']
			formulario.save()
			anio=request.POST['fecha_nacimiento_year']
			mes=request.POST['fecha_nacimiento_month']
			dia=request.POST['fecha_nacimiento_day']
			fecha_nacimiento=anio+"-"+mes+"-"+dia
			imagen=request.FILES['imagen']
			sexo=request.POST['sexo']
			ci=request.POST['ci']
			telefono=request.POST['telefono']
			nuevo_usuario=User.objects.get(username=usuario)
			perfil=Admin.objects.create(user=nuevo_usuario,fecha_nacimiento=fecha_nacimiento,imagen=imagen,sexo=sexo,ci=ci,telefono=telefono)
			return HttpResponseRedirect("/login_admin/")
	else:
		formulario=UserCreationForm()
		formulario2=fadmin()
	return render_to_response('registro_admin.html',{'formulario':formulario,'formulario2':formulario2},context_instance=RequestContext(request))

def login_admin(request):
	if request.method=="POST":
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario=request.POST['username']
			contrasena=request.POST['password']
			acceso=authenticate(username=usuario, password=contrasena)
			if acceso is not None:
					login(request, acceso)
					return HttpResponseRedirect("/user/admin/")
		else:
			return HttpResponse("Error en los datos")
	else:
		formulario=AuthenticationForm()
	return render_to_response("login_admin.html", {"formulario":formulario}, context_instance=RequestContext(request))

def perfil_admin(request):
	usuario=request.user
	u=User.objects.get(username=usuario)
	a=Admin.objects.get(user=u)
	return render_to_response("perfil_admin.html",{'a':a},context_instance=RequestContext(request))

def error_permit(request):
	return render_to_response("error_permit.html",{},RequestContext(request))

def permisos(request):
	listapermisos=[]
	lista=request.user.user_permissions.all()

def _adminPermisos(request):
	permisosGlobale=permisos_s()
	lista=permisos(request)
	render_to_response("")

def permisos_s():
	listagenerica=[]
	#listagenerica.append({"id":"usuarios.ver_blog"})
	return listagenerica