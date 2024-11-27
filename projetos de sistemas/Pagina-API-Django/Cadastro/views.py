from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Login, Cadastrar, Perfil, Contato, Exercicios, Planos
from .serializers import LoginSerializer, CadastrarSerializer, PerfilSerializer, ContatoSerializer, ExerciciosSerializer, PlanosSerializer

import json



@api_view(['GET'])
def get_logins(request):
    
    if request.method == 'GET':
        
        logins = Login.objects.all()
        
        serializer = LoginSerializer(logins, many=True)
        
        return Response(serializer.data)
        
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def get_by_login(request, usuario):

    try:
        login = Login.objects.get(pk=usuario)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = LoginSerializer(login)
        return Response(serializer.data)

       

    

@api_view(['GET','POST','PUT','DELETE'])
def login_manager(request):
    
    if request.method == 'GET':
        
        logins = Login.objects.all()
        
        serializer = LoginSerializer(logins, many=True)
        
        return Response(serializer.data)
        
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

# ACESSOS

    if request.method == 'GET':

        try:
            if request.GET['login']:                         # Check if there is a get parameter called 'user' (/?user=xxxx&...)

                usuario = request.GET['login']         # Find get parameter

                try:
                    login = Login.objects.get(pk=usuario)   # Get the object in database
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = LoginSerializer(login)           # Serialize the object data into json
                return Response(serializer.data)            # Return the serialized data

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

# CRIANDO DADOS

    if request.method == 'POST':

        new_login = request.data
        
        serializer = LoginSerializer(data=new_login)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)




# EDITAR DADOS (PUT)

    if request.method == 'PUT':

        usuario = request.data['usuario']

        try:
            updated_login = Login.objects.get(pk=usuario)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = LoginSerializer(updated_login, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)




# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':

        try:
            login_to_delete = Login.objects.get(pk=request.data['usuario'])
            login_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
        

@api_view(['GET','POST','PUT','DELETE'])
def cadastrar_manager(request):
    
    if request.method == 'GET':
        
        cadastros = Cadastrar.objects.all()
        
        serializer = CadastrarSerializer(cadastros, many=True)
        
        return Response(serializer.data)
        
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

# ACESSOS

    if request.method == 'GET':

        try:
            if request.GET['cadastrar']:                         

                usuario = request.GET['cadastrar']         

                try:
                    cadastro = Cadastrar.objects.get(pk=usuario)   
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = CadastrarSerializer(cadastro)           
                return Response(serializer.data)            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

# CRIANDO DADOS

    if request.method == 'POST':

        new_cadastro = request.data
        
        serializer = CadastrarSerializer(data=new_cadastro)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)




# EDITAR DADOS (PUT)

    if request.method == 'PUT':

        usuario = request.data['usuario']

        try:
            updated_cadastro = Cadastrar.objects.get(pk=usuario)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = CadastrarSerializer(updated_cadastro, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':

        try:
            cadastro_to_delete = Cadastrar.objects.get(pk=request.data['usuario'])
            cadastro_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
        
@api_view(['GET','POST','PUT','DELETE'])
def perfil_manager(request):
    
    
    if request.method == 'GET':
        
        perfil = Perfil.objects.all()
        
        serializer = PerfilSerializer(perfil, many=True)
        
        return Response(serializer.data)
        
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

# ACESSOS

    if request.method == 'GET':

        try:
            if request.GET['perfil']:                         

                usuario = request.GET['perfil']         

                try:
                    perfil = Perfil.objects.get(pk=usuario)   
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = PerfilSerializer(perfil)           
                return Response(serializer.data)            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

# CRIANDO DADOS

    if request.method == 'POST':

        new_perfil = request.data
        
        serializer = PerfilSerializer(data=new_perfil)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)




# EDITAR DADOS (PUT)

    if request.method == 'PUT':

        usuario = request.data['usuario']

        try:
            updated_perfil = Perfil.objects.get(pk=usuario)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = PerfilSerializer(updated_perfil, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)




# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':

        try:
            perfil_to_delete = Perfil.objects.get(pk=request.data['usuario'])
            perfil_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PUT','DELETE'])
def contato_manager(request):
    
    if request.method == 'GET':
        
        contato = Contato.objects.all()
        
        serializer = ContatoSerializer(contato, many=True)
        
        return Response(serializer.data)
        
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

# ACESSOS

    if request.method == 'GET':

        try:
            if request.GET['contato']:                         

                usuario = request.GET['contato']         

                try:
                    contato = Contato.objects.get()   
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = ContatoSerializer(contato)           
                return Response(serializer.data)            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

# CRIANDO DADOS

    if request.method == 'POST':

        new_contato = request.data
        
        serializer = ContatoSerializer(data=new_contato)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)




# EDITAR DADOS (PUT)

    if request.method == 'PUT':

        usuario = request.data['contato']

        try:
            updated_contato = Contato.objects.get()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = ContatoSerializer(updated_contato, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)




# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':

        try:
            contato_to_delete = Contato.objects.get()
            contato_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST','PUT','DELETE'])
def exercicios_manager(request):
    
    if request.method == 'GET':
        
        exercicio = Exercicios.objects.all()
        
        serializer = ExerciciosSerializer(exercicio, many=True)
        
        return Response(serializer.data)
        
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

# ACESSOS

    if request.method == 'GET':

        try:
            if request.GET['nome']:                         

                usuario = request.GET['nome']         

                try:
                    exercicio = Exercicios.objects.get(pk=usuario)   
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = ExerciciosSerializer(exercicio)           
                return Response(serializer.data)            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

# CRIANDO DADOS

    if request.method == 'POST':

        new_exercicio = request.data
        
        serializer = ExerciciosSerializer(data=new_exercicio)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)




# EDITAR DADOS (PUT)

    if request.method == 'PUT':

        usuario = request.data['nome']

        try:
            updated_exercicio = Exercicios.objects.get(pk=usuario)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = ExerciciosSerializer(updated_exercicio, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)




# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':

        try:
            exercicio_to_delete = Contato.objects.get()
            exercicio_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        
@api_view(['GET','POST','PUT','DELETE'])
def planos_manager(request):
    
    if request.method == 'GET':
        
        plano = Planos.objects.all()
        
        serializer = PlanosSerializer(plano, many=True)
        
        return Response(serializer.data)
        
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

# ACESSOS

    if request.method == 'GET':

        try:
            if request.GET['nome']:                         

                usuario = request.GET['nome']         

                try:
                    plano = Planos.objects.get(pk=usuario)   
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = PlanosSerializer(plano)           
                return Response(serializer.data)            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

# CRIANDO DADOS

    if request.method == 'POST':

        new_plano = request.data
        
        serializer = PlanosSerializer(data=new_plano)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)




# EDITAR DADOS (PUT)

    if request.method == 'PUT':

        usuario = request.data['nome']

        try:
            updated_plano = Planos.objects.get(pk=usuario)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = PlanosSerializer(updated_plano, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)




# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':

        try:
            plano_to_delete = Planos.objects.get()
            plano_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)        