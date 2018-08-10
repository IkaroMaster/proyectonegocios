#coding: utf8
from django.shortcuts import render

from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.template.defaultfilters import timesince,linebreaks

from django.contrib.staticfiles.templatetags.staticfiles import static




@login_required
def home(request):

	tweets = Tweet.objects.all().order_by('-fecha_publicacion')



	# perfil_tweet = Perfil.objects.filter(usuario = tweets.usuario)
	# perfil_tweet = User.objects.select_related('Perfil','Tweet')
	soy_receptor = Perfil.objects.get(usuario = request.user)

	# chat = Chat.objects.filter(Q(receptor = soy_receptor ) & ~Q(emisor = request.user) |Q(emisor= request.user)).order_by('-fecha_envio')


	
	perfil = Perfil.objects.get(usuario = request.user)
	chat = Chat2.objects.filter(Q(perfiles =perfil)).order_by('-ultimo_mensaje')

	tweets_publicados = Tweet.objects.filter(perfil = perfil)

	siguiendo = Siguiendo.objects.get(usuario = request.user)


	if siguiendo.seguidos.all().count() > 0:
		for p in siguiendo.seguidos.all():	
	 		perfiles = Perfil.objects.exclude(usuario = p.usuario)
	else:
		perfiles = Perfil.objects.all()

	# perfiles = Perfil.objects.all().exclude(usuario__in= siguiendo.seguidos.all().usuario)

	# perfiles = Perfil.objects.filter().exclude(usuario = )

	# perfiles = Perfil.objects.all()

	perfiles_siguiendome = Siguiendo.objects.filter(seguidos=perfil)

	# formTweet = TweetForm(initial={'usuario' : request.user})
	formTweet = TweetForm(initial={'perfil' : perfil})

	
	
	for f in formTweet.fields:
		formTweet.fields[f].widget.attrs['class'] = 'form-control'

	
	
	ctx = {
		'chat' : chat,
		'tweets' : tweets,
		'formTweet' : formTweet,
		'perfil' : perfil,
		'perfiles' : perfiles,
		'seguidos' :siguiendo,
		'perfiles_siguiendome' : perfiles_siguiendome,
		'tweets_publicados' : tweets_publicados,

		# 'perfil_tweet' :perfil_tweet,
	}
	return render(request,'home.html',ctx)


@login_required()
def perfil(request,id):
	perfil = Perfil.objects.get(pk = id)
	usuarios = Perfil.objects.all()
	
	tweets_publicados = Tweet.objects.filter(perfil = perfil).order_by('-fecha_publicacion')
	seguidos = Siguiendo.objects.filter(usuario = perfil.usuario)
	perfiles_siguiendome = Siguiendo.objects.filter(seguidos=perfil)
	ctx = {
		'usuarios':usuarios,
		'perfil' : perfil,
		'seguidos' :seguidos,
		'perfiles_siguiendome' : perfiles_siguiendome,
		'tweets_publicados' : tweets_publicados,

	}

	return render(request,'perfil.html',ctx)

@login_required()
def siguiendo(request,id):
	perfil = Perfil.objects.get(pk = id)
	usuarios = Perfil.objects.all()
	
	
	siguiendo = Siguiendo.objects.get(usuario = perfil.usuario)
	siguiendo_yo = Siguiendo.objects.get(usuario = request.user)

	if siguiendo_yo.seguidos.all().count() > 0:
		for p in siguiendo_yo.seguidos.all():	
	 		perfiles = Perfil.objects.all().exclude(usuario = p.usuario)

	else:
		perfiles = Perfil.objects.all()


	perfiles_siguiendome = Siguiendo.objects.filter(seguidos=perfil)
	ctx = {
		'usuarios':usuarios,
		'perfil' : perfil,
		'seguidos' :siguiendo,
		'siguiendo_yo' :siguiendo_yo,
		'perfiles_siguiendome' : perfiles_siguiendome,
		'perfiles' : perfiles,
		

	}

	return render(request,'siguiendo.html',ctx)




@login_required()
def mensaje(request):
	id = request.GET.get('id_recibido')
	chat = Chat2.objects.get(pk = id)
	mensajes = Mensaje.objects.filter(chat = chat).order_by('enviado')

	html = ''

	if mensajes.count() == 0:
		html += 'No hay resultados para la búsqueda: <strong>{}</strong>'.format(id)
		return JsonResponse({'result': html})
	else:
		for m in mensajes:
			perfil = Perfil.objects.get(usuario = m.usuario)
			if m.usuario == request.user:
				html += '''
				<div class="d-flex justify-content-end">
					
					<div class="col-md-auto m-2 p-2  " style="background-color: #E8F4FA; border-radius: 6px;border-bottom-left-radius: 30px;  "><p >{1}</p></div>
					<div class="col-md-1">
						<img src="{0}" alt="{0}" width="20px" style="border-radius:100%;">
					</div>
					
				</div>
				''' .format(perfil.avatar.url,m.mensaje)
			else:
				html += '''
				<div class="row">
					<div class="col-md-1">
						<img src="{0}" alt="{0}" width="20px" style="border-radius:100%;">
					</div>
					<div class="col-md-auto m-2 p-2" style="background-color: #E6ECF0; border-radius: 6px;border-bottom-right-radius: 30px;  "><p>{1}</p></div>
					
				</div>
				''' .format(perfil.avatar.url,m.mensaje)

		formMensaje = MensajeForm(initial={'usuario': request.user,'chat':chat})
		for f in formMensaje.fields:
			formMensaje.fields[f].widget.attrs['class'] = 'form-control'
		html2 = ''
		html2 +='''
		
				    {0}
	
		'''.format(formMensaje)
					
		
		
		return JsonResponse({'result': html,'result2':html2})

@login_required()
def comentario(request):
	id = request.GET.get('id_recibido')
	tweet = Tweet.objects.get(pk= id)
	perfilTweet = Perfil.objects.get(pk = tweet.perfil.id)



	htmlTweet = ''
	htmlTweet += '''
				<div id="idTweetComentario" data-id="{0}" class="row">
					<div class="col-md-2">
						<img src="/media/{1}" alt="{1}" width="100%" style="border-radius:100%" >
					</div>
					<div class="col-md-10">
						<a href="" style="color:black;">
							<span><strong>{2}</strong></span>
						</a><span class="text-muted">@{3}</span> .

							<span class="text-muted">{4}</span>
						
						<br>
						<p>{5}</p>
					</div>

					<div class="col-md-1"></div>
					<div class="col-md-11">
						<img src="" alt="Si existe imagen" width="100%">
					</div>
					
				</div>

	''' .format(id,
				perfilTweet.avatar,
				perfilTweet.usuario.get_full_name(),
				perfilTweet.usuario,
				tweet.fecha_publicacion,
				tweet.contenido)

	# htmlTweet += '''
	# 		<div id="idTweetComentario" data-id="{3}" class="row">
	# 			<div class="col-md-2">
	# 				<img src="/media/{2}" alt="Photo" style="border-radius:100%;" width="100%" >	
	# 			</div>
	# 			<div class="col-md-8">
	# 				<strong>{0}</strong>
	# 				<p>{1}</p>
	# 			</div>
	# 			<br>
	# 		</div>
	# ''' .format(perfilTweet.usuario,tweet.contenido,perfilTweet.avatar,id)


	perfil = Perfil.objects.get(usuario = request.user)
	formComentario = ComentarioForm(initial={'perfil' : perfil,'tweet':tweet})
	htmlComentario = ''
	htmlComentario += '''

	{0}

	''' .format(formComentario)
	# if request.method == 'POST':
	# 	form = ComentarioForm(data = request.POST)
	# 	if form.is_valid():
	# 		c = form.save() 
	
	
	htmlUsuarioComentario = '''{0}''' .format(perfilTweet.usuario)
		
	
	return JsonResponse({'result': htmlTweet,'result2':htmlComentario,'result3':htmlUsuarioComentario})



def comentarios(request):
	id = request.GET.get('id_recibido')
	tweet = Tweet.objects.get(pk= id)
	perfilTweet = Perfil.objects.get(pk = tweet.perfil.id)



	htmlTweet = ''
	htmlTweet += '''
				<div id="idTweetComentarios" data-id="{0}" class="row">
					<div class="col-md-2">
						<img src="/media/{1}" alt="{1}" width="100%" style="border-radius:100%" >
					</div>
					<div class="col-md-10">
						<a href="" style="color:black;">
							<span><strong>{2}</strong></span>
						</a><span class="text-muted">@{3}</span> .

							<span class="text-muted">{4}</span>
						
						<br>
						<p>{5}</p>
					</div>

					<div class="col-md-1"></div>
					<div class="col-md-11">
						<img src="" alt="Si existe imagen" width="100%">
					</div>
					
				</div>

	''' .format(id,
				perfilTweet.avatar,
				perfilTweet.usuario.get_full_name(),
				perfilTweet.usuario,
				tweet.fecha_publicacion,
				tweet.contenido)

	


	perfil = Perfil.objects.get(usuario = request.user)
	formComentario = ComentarioForm(initial={'perfil' : perfil,'tweet':tweet})
	htmlComentario = ''
	htmlComentario += '''

	{0}

	''' .format(formComentario)
	
	htmlComentarios = ''
	comentario = Comentario.objects.filter(tweet = tweet).order_by('-fecha_publicacion')
	for c in comentario:
		
		htmlComentarios += '''

					<div id="idTweetComentarios" data-id="{0}" class="row">
						<div class="col-md-2">
							<img src="/media/{1}" alt="{1}" width="100%" style="border-radius:100%" >
						</div>
						<div class="col-md-10">
							<a href="" style="color:black;">
								<span><strong>{2}</strong></span>
							</a><span class="text-muted">@{3}</span> .

								<span class="text-muted">{4}</span>
							
							<br>
							<p>{5}</p>
						</div>

						
						
					</div>
					<hr>

		'''  .format(c.id,
				c.perfil.avatar,
				c.perfil.usuario.get_full_name(),
				c.perfil.usuario,
				c.fecha_publicacion,
				c.contenido)

	
	return JsonResponse({'result': htmlTweet,'result2':htmlComentario,'result3':htmlComentarios})

@login_required()
def enviar_mensaje(request):
	form = MensajeForm(data = request.POST)

	if form.is_valid():
		m = form.save()

		perfil = Perfil.objects.get(usuario = request.user)

		html = ''
		html += '''
		<div class="d-flex justify-content-end">
			
			<div class="col-md-auto m-2 p-2  " style="background-color: #E8F4FA; border-radius: 6px;border-bottom-left-radius: 30px;  "><p >{1}</p></div>
			<div class="col-md-1">
				<img src="{0}" alt="{0}" width="20px" style="border-radius:0%;">
			</div>
			
		</div>
		''' .format(perfil.avatar.url,m.mensaje)

		return JsonResponse({'respuesta_del_servidor': html })


@login_required()
def enviar_tweet(request):
	form = TweetForm(data = request.POST)

	if form.is_valid():
		t = form.save()

		# com =''
		# com += '''
		# 	<div class="row" id="idChat" data-id"%s">
		# 		<p>%s--- </p>
		# 		<p class="card">%s</p>
		# 		<p>%s</p>
		# 	</div>

		# 	'''%(id,m.usuario,m.mensaje,m.enviado)

		return JsonResponse({'respuesta_del_servidor': 'enviado' })

@login_required()
def enviar_comentario(request):
	 # form_r = request.POST.get('form')
	 # id = request.GET.get('id_recibido')
	form = ComentarioForm(data = request.POST)

	if form.is_valid():
		c = form.save()

		idTweet = c.tweet.id
		tweet = Tweet.objects.get(pk = idTweet)
		html = ''
	
		html += '''
			{0}

		''' .format(tweet.comentario_set.count())

		html2 = '' 
		html2 += '''
			<hr>
			<div id="idTweetComentarios" data-id="{0}" class="row">
				<div class="col-md-2">
					<img src="/media/{1}" alt="{1}" width="100%" style="border-radius:100%" >
				</div>
				<div class="col-md-10">
					<a href="" style="color:black;">
						<span><strong>{2}</strong></span>
					</a><span class="text-muted">@{3}</span> .

						<span class="text-muted">{4}</span>
					
					<br>
					<p>{5}</p>
				</div>

						
						
			</div>
			<hr>

		''' .format(c.id,
				c.perfil.avatar,
				c.perfil.usuario.get_full_name(),
				c.perfil.usuario,
				c.fecha_publicacion,
				c.contenido)

		# com =''
		# com += '''
		# 	<div class="row" id="idChat" data-id"%s">
		# 		<p>%s--- </p>
		# 		<p class="card">%s</p>
		# 		<p>%s</p>
		# 	</div>
		# 	'''%(id,m.usuario,m.mensaje,m.enviado)

		return JsonResponse({'respuesta_del_servidor': html,'result2':html2 })

@login_required()
def like(request):
	id = request.GET.get('id_recibido')

	tweet = Tweet.objects.get(pk= id)
	perfil = Perfil.objects.get(usuario = request.user)

	likes = Like.objects.filter(tweet=tweet,like=perfil)
	like = Like.objects.filter(tweet= tweet)
	# form = LikeForm(initial={'tweet':tweet,'like':perfil})
	html = ''
	html2 = ''
	if len(likes) > 0:
		urlImgLike = static('img/like.png')
		likes.delete()
		if like.count() > 0 :
			html += '''
				<h5 style="margin-top:7px;color:gray;"  >
							{0}
				</h5>
			''' .format(like.count())
		else:
			html+=''' '''

		html2 = '''
				<img src="{0}" alt="" width="40px"></div>
		''' .format(urlImgLike)
		return JsonResponse({'result': html,'result2':html2 })

		
	else:	
		urlImgLike = static('img/like2.png')
		guardarLike = Like(tweet=tweet,like=perfil)  
		c = guardarLike.save()

		html += '''
			<h5 style="margin-top:7px;color:red;"  >
						{0}
			</h5>
		''' .format(like.count())

		html2 = '''
				<img src="{0}" alt="" width="25px"></div>
		''' .format(urlImgLike)

		return JsonResponse({'result': html,'result2':html2 })
	# if form.is_valid():
	# 	

	

@login_required()
def seguir(request):
	id = request.GET.get('id_envio')
	perfil = Perfil.objects.get(pk = id)

	seguir = Siguiendo.objects.get(usuario = request.user)

	if Siguiendo.objects.filter(usuario = request.user) is not None:

		ya_sigo = Siguiendo.objects.filter(usuario = request.user,seguidos = perfil).exists()

		if ya_sigo:	
			seguir.seguidos.remove(perfil)
			result = 'unfollow'

			if seguir.seguidos.all():
				html = '''
					{0}
				''' .format(seguir.seguidos.count())
			else:
				html = '''0'''

		else:
			seguir.seguidos.add(perfil)
			result = 'follow'
			if seguir.seguidos.all():
				html = '''
					{0}
				''' .format(seguir.seguidos.count())
			else:
				html = '''0'''

		return JsonResponse({'result':result,'result2':html})

	else:
		 s = Siguiendo(usuario = request.user,seguidos = perfil)
		 g =s.save() 
		 return JsonResponse({'result':'guardado'})


@login_required()
def seguir_usuario(request):
	id = request.GET.get('id_envio')
	usuario = User.objects.get(pk=id)
	perfil = Perfil.objects.get(usuario = usuario)

	seguir = Siguiendo.objects.get(usuario = request.user)

	if Siguiendo.objects.filter(usuario = request.user) is not None:

		ya_sigo = Siguiendo.objects.filter(usuario = request.user,seguidos = perfil).exists()

		if ya_sigo:	
			seguir.seguidos.remove(perfil)
			result = 'unfollow'

			if seguir.seguidos.all():
				html = '''
					{0}
				''' .format(seguir.seguidos.count())
			else:
				html = '''0'''

		else:
			seguir.seguidos.add(perfil)
			result = 'follow'
			if seguir.seguidos.all():
				html = '''
					{0}
				''' .format(seguir.seguidos.count())
			else:
				html = '''0'''

		return JsonResponse({'result':result,'result2':html})

	else:
		 s = Siguiendo(usuario = request.user,seguidos = perfil)
		 g =s.save() 
		 return JsonResponse({'result':'guardado'})

