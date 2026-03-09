from rest_framework import serializers
from .models import Pedido, ItemPedido, Tamanho, Sabores, Acompanhamentos

class ItemPedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemPedido
        fields = ['tamanho', 'sabores', 'acompanhamentos']

    def validate(self, data):
        tamanho = data['tamanho']
        sabores = data['sabores']
        acompanhamentos = data['acompanhamentos']

        if len(sabores) > tamanho.max_sabores:
            raise serializers.ValidationError(
                f"O tamanho {tamanho.nome} permite no máximo {tamanho.max_sabores} sabores."
                ) 
            
        return data
    
class PedidoSerializer(serializers.ModelSerializer):

    itens = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['nome_cliente', 'endereco', 'forma_pagamento', 'itens']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')

        pedido = Pedido.objects.create(**validated_data)

        for item_data in itens_data:
            sabores = item_data.pop('sabores')
            acompanhamentos = item_data.pop('acompanhamentos')
            item = ItemPedido.objects.create(pedido=pedido, **item_data)
            item.sabores.set(sabores)
            item.acompanhamentos.set(acompanhamentos)

        return pedido  
        
            