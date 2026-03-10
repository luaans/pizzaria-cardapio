from rest_framework import serializers
from .models import (
    Pedido,
    ItemPedido,
    Tamanho,
    Sabores,
    Bordas,
    Bebidas
)


# =========================
# ITEM DO PEDIDO
# =========================

class ItemPedidoSerializer(serializers.ModelSerializer):

    sabores = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Sabores.objects.all()
    )

    tamanho = serializers.PrimaryKeyRelatedField(
        queryset=Tamanho.objects.all()
    )

    class Meta:
        model = ItemPedido
        fields = ['tamanho', 'sabores', 'quantidade']

    def validate(self, data):

        tamanho = data['tamanho']
        sabores = data['sabores']

        if len(sabores) > tamanho.max_sabores:
            raise serializers.ValidationError(
                f"O tamanho {tamanho.nome} permite no máximo {tamanho.max_sabores} sabores."
            )

        return data


# =========================
# PEDIDO
# =========================

class PedidoSerializer(serializers.ModelSerializer):

    itens = ItemPedidoSerializer(many=True)

    bordas = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Bordas.objects.all(),
        required=False
    )

    bebidas = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Bebidas.objects.all(),
        required=False
    )

    total = serializers.ReadOnlyField()

    class Meta:
        model = Pedido
        fields = [
            'id',
            'nome_cliente',
            'telefone',
            'endereco',
            'forma_pagamento',
            'itens',
            'bordas',
            'bebidas',
            'total'
        ]

    def create(self, validated_data):

        itens_data = validated_data.pop('itens')
        bordas = validated_data.pop('bordas', [])
        bebidas = validated_data.pop('bebidas', [])

        pedido = Pedido.objects.create(**validated_data)

        # cria itens do pedido
        for item_data in itens_data:
            sabores = item_data.pop('sabores')

            item = ItemPedido.objects.create(
                pedido=pedido,
                **item_data
            )

            item.sabores.set(sabores)

        # adiciona bordas
        pedido.bordas.set(bordas)

        # adiciona bebidas
        pedido.bebidas.set(bebidas)

        return pedido