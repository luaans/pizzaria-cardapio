
from django.contrib import admin

from .models import Acompanhamentos, ItemPedido, Pedido, Sabores, Tamanho


@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "max_sabores")
    search_fields = ("nome",)
    list_filter = ("max_sabores",)


@admin.register(Sabores)
class SaboresAdmin(admin.ModelAdmin):
    list_display = ("nome", "disponivel")
    search_fields = ("nome",)
    list_filter = ("disponivel",)


@admin.register(Acompanhamentos)
class AcompanhamentosAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "disponivel")
    search_fields = ("nome",)
    list_filter = ("disponivel",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome_cliente", "telefone", "forma_pagamento", "criado_em")
    search_fields = ("nome_cliente", "telefone")
    list_filter = ("forma_pagamento", "criado_em")
    readonly_fields = ("criado_em",)


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "tamanho", "sabores_list")
    list_filter = ("tamanho",)

    def sabores_list(self, obj):
        return ", ".join([sabor.nome for sabor in obj.sabores.all()])

    sabores_list.short_description = "Sabores"
