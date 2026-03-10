from django.contrib import admin

from .models import (
    ItemPedido,
    Pedido,
    Sabores,
    Tamanho,
    CategoriaSabor,
    PrecoPizza,
    Bordas,
    Bebidas
)


@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ("nome", "max_sabores")
    search_fields = ("nome",)
    list_filter = ("max_sabores",)


@admin.register(Sabores)
class SaboresAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "disponivel")
    search_fields = ("nome",)
    list_filter = ("categoria", "disponivel")


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


@admin.register(Bordas)
class BordasAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "disponivel")
    search_fields = ("nome",)
    list_filter = ("disponivel",)


@admin.register(Bebidas)
class BebidasAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "disponivel")
    search_fields = ("nome",)
    list_filter = ("disponivel",)


@admin.register(CategoriaSabor)
class CategoriaSaborAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(PrecoPizza)
class PrecoPizzaAdmin(admin.ModelAdmin):
    list_display = ("categoria", "tamanho", "preco")
    list_filter = ("categoria", "tamanho")
    search_fields = ("categoria__nome", "tamanho__nome")