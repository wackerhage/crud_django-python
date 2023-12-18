from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    pais_trabalho = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
