from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
# Create your models here.

@python_2_unicode_compatible
class Perfil(models.Model):
	usuario				= models.OneToOneField(User)
	avatar				= models.ImageField(upload_to='avatares',null=True,blank=True)
	portada 			= models.ImageField(upload_to='portadas',null=True,blank=True)
	fecha_nacimiento	= models.DateField(null=True,blank=True)
	biografia			= models.CharField(max_length=200,null=True,blank=True)
	sitioweb			= models.EmailField(blank=True,null=True)
	pais 				= models.CharField(max_length=200,null=True,blank=True)


	SEXOS = (('F','Femenino'),('M','Masculino'))
	genero 				= models.CharField(max_length=1,choices=SEXOS,default='M')

	# tweet = models.ForeignKey(Tweet)

	def __str__(self):
		return "{} --> {}" .format(self.usuario,self.genero)

@python_2_unicode_compatible
class Siguiendo(models.Model):
	usuario  	= models.ForeignKey(User)
	seguidos 	= models.ManyToManyField(Perfil,blank=True)

	def __str__(self):
		return "{}" .format(self.usuario)





@python_2_unicode_compatible
class Tweet(models.Model):
	# usuario 			= models.ForeignKey(User)
	perfil 				= models.ForeignKey(Perfil,on_delete=models.CASCADE)
	contenido 			= models.CharField(max_length=140,verbose_name='')
	multimedia 			= models.ImageField(upload_to='foto_tweet',blank=True,null=True)
	fecha_publicacion 	= models.DateTimeField(auto_now_add=True)
	# like 				= models.ManyToManyField(User,blank=True)
	es_retweet 			= models.BooleanField(default=False)
	#user 				= models.ForeignKey(User,blank=True)
	# estweet 				= models.ForeignKey(Tweet,blank=True)

	# comentario 			= models.ManyToManyField(Comentario,blank=True)
	# like 				= models.OneToOneField(Like,blank=True,null=True)

	def __str__(self):
		return self.contenido

@python_2_unicode_compatible
class Like(models.Model):
	# tweet = models.OneToOneField(Tweet)
	tweet 	= models.ForeignKey(Tweet)
	like 	= models.ForeignKey(Perfil)
	fecha_like = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "{} -- >{}" .format(self.tweet,self.like)


@python_2_unicode_compatible
class Comentario(models.Model):
	tweet 				= models.ForeignKey(Tweet)
	perfil				= models.ForeignKey(Perfil)
	contenido			= models.TextField(max_length=140,verbose_name='')
	fecha_publicacion 	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{}" .format(self.contenido)



@python_2_unicode_compatible
class Retweet(models.Model):
	tweet 				= models.ForeignKey(Tweet)
	perfil 			    = models.ForeignKey(Perfil,on_delete=models.CASCADE)
	comentario 			= models.CharField(max_length=140)
	fecha_publicacion	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{} --> {}" .format(self.tweet,self.comentario)

	


# @python_2_unicode_compatible
# class Chat(models.Model):
# 	fecha_envio 	= models.DateTimeField(auto_now_add=True)
# 	mensaje 		= models.CharField(max_length=1000)
# 	emisor			= models.ForeignKey(User)
# 	receptor		= models.ForeignKey(Perfil)
# 	# enviado 		= models.BooleanField(default=False)

# 	def __str__(self):
# 		return "{} -> {} = {} ({})" .format(self.emisor,self.receptor,self.mensaje,self.fecha_envio)



#-------------------------------------------------
#-------------------------------------------------

@python_2_unicode_compatible
class Chat2(models.Model):
	nombre = models.CharField(max_length=20,blank=True)
	perfiles = models.ManyToManyField(Perfil)
	ultimo_mensaje = models.DateTimeField(auto_now=True)


	def __str__(self):
		return "{}" .format(self.nombre)

@python_2_unicode_compatible
class Mensaje(models.Model):
	chat = models.ForeignKey(Chat2)
	usuario = models.ForeignKey(User)
	mensaje = models.TextField(verbose_name='')
	enviado = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "{} {}" .format(self.usuario,self.mensaje)

#-------------------------------------------------
#-------------------------------------------------
# @python_2_unicode_compatible
# class Amigo(models.Model):
# 	usuario		= models.ForeignKey(User)
# 	siguiendo	= models.ManyToManyField(Perfil)

# 	def __str__(self):
# 		return "{}" .format(self.usuario)






