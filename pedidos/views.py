from django.shortcuts import render
from rest_framework import generics
from .models import Pedido
from .serializers import PedidoSerializer

class CriarPedidoView(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer