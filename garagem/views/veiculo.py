from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from garagem.models import Veiculo
from garagem.serializers import VeiculoSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
