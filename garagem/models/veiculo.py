from django.db import models
from garagem.models import Cor, Modelo, Acessorio
from uploader.models import Image

class Veiculo (models.Model):
    cor = models.ForeignKey (Cor, on_delete=models.CASCADE)
    modelo = models.ForeignKey (Modelo, on_delete=models.CASCADE)
    ano = models.IntegerField()
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    acessorio = models.ManyToManyField(Acessorio, related_name="+")
    image = models.ManyToManyField(Image, related_name="+")

    def __str__ (self):
        return self.descricao