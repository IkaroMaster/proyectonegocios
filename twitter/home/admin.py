from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Perfil)
admin.site.register(Tweet)
admin.site.register(Comentario)
admin.site.register(Retweet)
# admin.site.register(Amigo)
admin.site.register(Siguiendo)
admin.site.register(Like)
# admin.site.register(Chat)
admin.site.register(Chat2)
admin.site.register(Mensaje)

