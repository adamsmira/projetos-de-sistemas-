from django.db import models

class Login(models.Model):
    
    usuario = models.CharField(max_length=20, primary_key=True, default='')
    senha = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return f'Usuario: {self.usuario} '
    
class Cadastrar(models.Model):
    usuario = models.CharField(max_length=20, primary_key=True, default='')
    senha = models.CharField(max_length=20, default='')
    email = models.EmailField(default='')
    telefone = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Usuario: {self.usuario} | Email: {self.email} '
        

class Perfil(models.Model):
    usuario = models.CharField(max_length=20, primary_key=True, default='')
    email = models.EmailField(default='')
    
class Contato(models.Model):
    nome = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    mensagem = models.CharField(max_length=1000, default='')
    
class Exercicios(models.Model):
    nome = models.CharField(max_length=100,  default='')
    descricao = models.CharField(max_length=1000, default='')
    
class Planos(models.Model):
    nome = models.CharField(max_length=100, default='')
    descricao = models.CharField(max_length=1000, default='')
    preco = models.FloatField(default=0)         
