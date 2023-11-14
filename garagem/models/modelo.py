from django.db import models
from garagem.models import Categoria, Marca
    
class Modelo (models.Model):
    Categoria = models.ForeignKey (Categoria, on_delete=models.CASCADE)
    Marca = models.ForeignKey (Marca, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome