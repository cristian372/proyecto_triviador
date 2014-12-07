from django.db import models

# Create your models here.
class Tema(models.Model):
	Tema=models.CharField(max_length=20,unique=True)
	def __str__(self):
		return self.Tema

class Pregunta(models.Model):
	Tema=models.ForeignKey(Tema)
	pregunta=models.CharField(max_length=200, null=False)
	def __str__(self):
		return self.Tema

class Respuesta(models.Model):
	respuesta_correcta=models.CharField(max_length=500)
	respusta_opcional=models.CharField(max_length=500)
	respusta_opciona2=models.CharField(max_length=500)
	respusta_opciona3=models.CharField(max_length=500)
	respusta_opciona4=models.CharField(max_length=500)
	respusta_opciona5=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
	def __str__(self):
		return self.pregunta