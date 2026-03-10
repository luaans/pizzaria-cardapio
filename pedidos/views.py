from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Pedido, Sabores, Tamanho, PrecoPizza
from .serializers import PedidoSerializer


class CriarPedidoView(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pedido = serializer.save()
        
        return Response(
            {
                "mensagem": "Pedido criado com sucesso",
                "pedido_id": pedido.id,
                "total": pedido.total
            },
            status=status.HTTP_201_CREATED
        )


@api_view(['GET'])
def cardapio(request):
    sabores = Sabores.objects.filter(disponivel=True).values()
    tamanhos = Tamanho.objects.all().values()
    precos = PrecoPizza.objects.all().values()

    return Response({
        "sabores": list(sabores),
        "tamanhos": list(tamanhos),
        "precos": list(precos)
    })