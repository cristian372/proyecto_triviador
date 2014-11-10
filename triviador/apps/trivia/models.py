from django.db import models

# Create your models here.
class Tema(models.Model):
	Tema=models.CharField(max_length=150, unique=True)
	materia=models.CharField(max_length=150)
	fecha=models.DateField(auto_now=True)
	def __unicode__(self):
		return "->%s "%(self.Tema)

class Pregunta(models.Model):
	Tema=models.ForeignKey(Tema)
	pregunta=models.CharField(max_length=200)
	respuesta=models.CharField(max_length=200)
	puntaje=models.IntegerField(null=True)
	fecha=models.DateField(auto_now=True)