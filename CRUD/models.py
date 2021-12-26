from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length = 200)
    ultimo_nome = models.CharField(max_length = 200)
    data_nascimento = models.DateField()
    profissao = models.CharField(max_length = 200)
    criado = models.DateTimeField

    @property
    def nome_completo(self):
        """
        retorna o nome completo

        """

        return f'{self.nome }{self.ultimo_nome}'
