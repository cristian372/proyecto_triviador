#encoding:utf-8

from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

lista_anios = range(2014,1900,-1)
CHOICES = (('1', 'Hombre',), ('2', 'Mujer',))
class fperfil(ModelForm):
		class Meta:
			model=Perfil
			exclude=['user']

class fusuario(UserCreationForm):
	username=forms.CharField(max_length=50,required=True,help_text=False,label="Nick")
	password2=forms.CharField(help_text=False,label="contrasenia de confirmacion", widget=forms.PasswordInput)
	first_name=forms.CharField(max_length=60,required=True,label="Nombre")
	last_name=forms.CharField(max_length=60,required=True,label="Apellido")
	email=forms.EmailField(max_length=150,required=True,label="Email")
	class Meta:
		model=User
		fields=("username","password1","password2","first_name","last_name","email")
	def save(self, commit=True):
		user=super(fusuario,self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.last_name=self.cleaned_data.get("last_name")
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return user

class fperfil_modificar(ModelForm):
		class Meta:
			model=Perfil
			exclude=['user']


class fadmin(ModelForm):
	fecha_nacimiento=forms.DateField(widget=SelectDateWidget(years=lista_anios))
	sexo=forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
	class Meta:
		model=Admin
		exclude = ['user']