from datetime import date
from django.core.paginator import Paginator

from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length = 200)
    ultimo_nome = models.CharField(max_length = 200)
    data_nascimento = models.DateField()
    profissao = models.CharField(max_length = 200)
    criado = models.DateTimeField(auto_now=True)


    @property
    def nome_completo(self):
        """
        retorna o nome completo

        """

        return f'{self.nome.title()} {self.ultimo_nome.title()}'

    @property
    def idade(self):
        idade = date.today() - self.data_nascimento
        idade /= 365.25
        return ((idade).days)

