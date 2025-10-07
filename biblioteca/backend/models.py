from django.db import models

class Autores(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateTimeField(auto_now_add = True)
    nacionalidade = model.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    ano_publicacao = models.DateTimeField(auto_now_add =True)    
    genero = models.CharField(max_length=100)

class emprestimo(models.Model):
    

#email = models.EmailField(unique=True)


