from django.conf.urls import url

from . import views

app_name = 'home'

urlpatterns = [

	url(r'^$', views.home, name='home-url'),
	url(r'^twitter/perfil/(?P<id>\d+)/$', views.perfil, name='perfil-url'),
	url(r'^twitter/siguiendo/(?P<id>\d+)/$', views.siguiendo, name='siguiendo-url'),

	url(r'^twitter/mensaje/$',views.mensaje,name='mensaje-url'),
	url(r'^twitter/enviar_mensaje/$',views.enviar_mensaje,name='enviar_mensaje-url'),
	url(r'^twitter/enviar_tweet/$',views.enviar_tweet,name='enviar_tweet-url'),

	url(r'^twitter/comentario/$',views.comentario,name='comentario-url'),
	url(r'^twitter/comentarios/$',views.comentarios,name='comentarios-url'),
	url(r'^twitter/enviar_comentario/$',views.enviar_comentario,name='enviar_comentario-url'),
	url(r'^twitter/like/$',views.like,name='like-url'),


	url(r'^twitter/seguir/$',views.seguir,name='seguir-url'),
	url(r'^twitter/seguir_usuario/$',views.seguir_usuario,name='seguir_usuario-url'),


	
	


]