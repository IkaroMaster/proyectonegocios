from django.conf.urls import url

from . import views

app_name = 'seguridad'

urlpatterns = [

	url(r'^iniciar_sesion/$',views.iniciar_sesion,name='iniciar_sesion-url'),
	url(r'^cerrar_sesion/$',views.cerrar_sesion,name='cerrar_sesion-url'),

]