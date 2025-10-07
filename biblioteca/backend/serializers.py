from rest_framework import serializers
from .models import Autor, Livro, emprestimo, Reserva, Multa, Categoria, Editora
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    id_usuario = UserSerializer(read_only=True)
    
    class Meta:
        model = Autor
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    
    class Meta:
        model = Livro
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    id_livro = LivroSerializer(read_only=True)
    id_usuario = UserSerializer(read_only=True)
    
    class Meta:
        model = emprestimo
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    id_livro = LivroSerializer(read_only=True)
    id_usuario = UserSerializer(read_only=True)
    
    class Meta:
        model = Reserva
        fields = '__all__'

class MultaSerializer(serializers.ModelSerializer):
    id_usuario = UserSerializer(read_only=True)
    
    class Meta:
        model = Multa
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    
class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'
