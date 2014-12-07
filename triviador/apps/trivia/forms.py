from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ftema(ModelForm):
	class Meta:
		model=Tema

class fpregunta(ModelForm):
	class Meta:
		model=Pregunta
		exclude=['tema']

class frespuesta(ModelForm):
	class Meta:
		model=Respuesta
		exclude=['pregunta']
