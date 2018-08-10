from django.forms import ModelForm
from .models import *
from django import forms

class TweetForm(ModelForm):
	class Meta:
		model = Tweet
		fields = '__all__'
		widgets = {
				'perfil' : forms.HiddenInput(),
				'es_retweet' : forms.HiddenInput(),
				'comentario' : forms.HiddenInput(),
				'like' : forms.HiddenInput(),
				}

class MensajeForm(ModelForm):
	class Meta:
		model = Mensaje
		fields = '__all__'
		widgets = {
				'chat' : forms.HiddenInput(),
				'usuario' : forms.HiddenInput(),
				'mensaje'		: forms.Textarea(attrs = {
        		'class' 	: 'form-control',
        		'autofocus' : 'autofocus',
        		'rows': 2,
        		'placeholder' : 'Aa',
        		})
				}


class ComentarioForm(ModelForm):
	class Meta:
		model = Comentario
		fields = '__all__'
		widgets = {
				'perfil' : forms.HiddenInput(),
				'tweet' : forms.HiddenInput(),
				'contenido'	: forms.Textarea(attrs = {
        		'class' 	: 'form-control ',
        		'rows': 2,
        		'cols': 60,
        		'placeholder' : 'Aa',
        		})
				}

class LikeForm(ModelForm):
	class Meta:
		model = Like
		fields = '__all__'
		# widgets = {
		# 		'perfil' : forms.HiddenInput(),
		# 		'tweet' : forms.HiddenInput(),
		# 		}
