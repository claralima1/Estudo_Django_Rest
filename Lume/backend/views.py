from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Producao
from .serializers import UsuarioSerializer, ProducaoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProducaoViewSet(viewsets.ModelViewSet):
    queryset = Producao.objects.all()
    serializer_class = ProducaoSerializer
