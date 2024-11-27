from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [    
    
    path('user/<str:usuario>', views.get_by_login),
    path('login/', views.login_manager, name='login_manager'),
    path('cadastro/', views.cadastrar_manager , name='cadastro_manager'),
    path('perfil/', views.perfil_manager , name='perfil_manager'),
    path('contato/', views.contato_manager , name='contato_manager'),
    path('exercicios/', views.exercicios_manager , name='exercicio_manager'),
    path('planos/', views.planos_manager , name='plano_manager'),
]

    
