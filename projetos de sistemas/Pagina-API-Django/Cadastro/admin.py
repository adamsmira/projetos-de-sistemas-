from django.contrib import admin

from .models import Login, Cadastrar, Perfil, Contato, Exercicios, Planos

admin.site.register(Login)
admin.site.register(Cadastrar)
admin.site.register(Perfil)
admin.site.register(Contato)
admin.site.register(Exercicios)
admin.site.register(Planos)
