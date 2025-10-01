from rest_framework import serializers

from .models import Usuario, Producao

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producao
        fields = "__all__"
