from django.urls import path
from .views import CriarPedidoView
from . import views

urlpatterns = [
    path('pedidos/', CriarPedidoView.as_view(), name='criar-pedido'),
    path('cardapio/', views.cardapio, name='cardapio'),
]