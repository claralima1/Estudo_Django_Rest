from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Usuario(User):
    nome = models.CharField("Nome", max_length=100)
    uf = models.CharField("UF", max_length=2, blank=True, null=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True, null=True)
    eh_produtor = models.BooleanField("É produtor", default=False)

    # Campos específicos de produtor
    biografia = models.CharField("Biografia", max_length=500, blank=True, null=True)
    contatos = models.TextField("Contatos", blank=True, null=True)
    links_externos = models.JSONField("Links externos", default=list, blank=True)
    data_ativacao_produtor = models.DateTimeField("Data ativação produtor", blank=True, null=True)

    def __str__(self):
        return self.nome

class Producao(models.Model):
    nome = models.CharField("Nome", max_length=100)
    descricao = models.CharField("Descrição", max_length=500)
    produtor = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Produtor",limit_choices_to={'eh_produtor': True})
    data_producao = models.DateField("Data de produção", default=date.today)
    elenco = models.CharField("Elenco", max_length=500)
    duracao = models.IntegerField("Duração (em minutos)", blank=True, null=True)
    link_producao = models.URLField("Link da produção", blank=True, null=True)
    img_cartaz = models.ImageField("Cartaz", upload_to="cartazes/", blank=True, null=True)
    img_banner = models.ImageField("Banner", upload_to="banners/", blank=True, null=True)

    def __str__(self):
        return self.nome
