from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateTimeField(auto_now_add = True)
    nacionalidade = models.CharField(max_length=100)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    ano_publicacao = models.DateTimeField(auto_now_add =True)    
    genero = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    id_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.id_livro.titulo
    
class Reserva(models.Model):
    id_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.id_livro.titulo
    
class Multa(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data_multa = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'Multa de {self.valor} para o livro {self.id_emprestimo.id_livro.titulo}'

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome