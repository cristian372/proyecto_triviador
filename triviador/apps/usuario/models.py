from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
	user=models.OneToOneField(User, unique=True)
	ciudad=models.CharField(max_length="30", null=True)
	avatar=ImageWithThumbsField(upload_to="img_user", sizes=((50,50),(200,200)))

class Admin(models.Model):
	user = models.ForeignKey(User, unique=True)
	fecha_nacimiento=models.DateField()
	imagen =models.ImageField(null=True,upload_to='img_usuario')
	sexo = models.IntegerField(null=False)
	ci=models.IntegerField(null=True,unique=True)
	telefono = models.IntegerField(null=True)

		