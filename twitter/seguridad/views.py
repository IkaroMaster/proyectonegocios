from django.shortcuts import render

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse



def login_form(request):

	formulario_login = AuthenticationForm()
	formulario_login.fields['username'].widget.attrs['class'] = 'form-control'
	formulario_login.fields['password'].widget.attrs['class'] = 'form-control'
	ctx = {
		'formulario' : formulario_login
	}
	return render(request,'login_form.html',ctx)

def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect(reverse('seguridad:login_form-url'))



def iniciar_sesion(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(data = request.POST)
		if formulario.is_valid():
			usuario = request.POST['username']
			contrasena = request.POST['password']

			user = authenticate(username = usuario, password = contrasena)

			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect(reverse('home:home-url'))
					# return HttpResponse('el login funciona')

				else:
					return HttpResponseRedirect(reverse('seguridad:login_form-url'))

			else:
				return HttpResponseRedirect(reverse('seguridad:login_form-url'))

		else:
			return HttpResponseRedirect(reverse('seguridad:login_form-url'))
	else:
		return HttpResponse('Utilize el metodo POST')


