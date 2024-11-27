from rest_framework import serializers

from .models import Login, Cadastrar, Perfil, Contato, Exercicios, Planos


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('__all__')
        
class CadastrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastrar
        fields = ('__all__')
        
class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('__all__')
        
class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ('__all__')
        
class ExerciciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicios
        fields = ('__all__')
        
class PlanosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planos
        fields = ('__all__')