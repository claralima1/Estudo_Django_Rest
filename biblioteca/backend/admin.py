from django.contrib import admin
from .models import Autor, Livro, Emprestimo, Reserva, Multa, Categoria, Editora

admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Emprestimo)
admin.site.register(Reserva)
admin.site.register(Multa)
admin.site.register(Categoria)
admin.site.register(Editora)
