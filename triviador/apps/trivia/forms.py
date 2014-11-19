from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class fTemas(ModelForm):
	class Meta:
		model=Tema

class fPreguntas(ModelForm):
	class Meta:
		model=Pregunta

class fMPreguntas(ModelForm):
	class Meta:
		model=Pregunta
		exclude=['Tema']