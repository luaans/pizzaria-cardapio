from django.urls import path
from .views import CriarPedidoView

urlpatterns = [
    path('pedido/', CriarPedidoView.as_view(), name='criar-pedido'),
]