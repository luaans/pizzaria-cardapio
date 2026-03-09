from django.db import models
from django.core.exceptions import ValidationError


# Criando o modelo para pizza 

class Tamanho(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    max_sabores = models.IntegerField() # quantidade de sabores a depender do tamanho da pizza
    
    def __str__(self):
        return self.nome

class CategoriaSabor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome    

class PrecoPizza(models.Model):
    categoria = models.ForeignKey(
        CategoriaSabor,
        on_delete=models.CASCADE
    )   

    tamanho = models.ForeignKey(
        Tamanho,
        on_delete=models.CASCADE
    )       

    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.categoria.nome} - {self.tamanho.nome}"
    
class Sabores(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)

    categoria = models.ForeignKey(
        CategoriaSabor,
        on_delete=models.CASCADE,
        related_name="sabores"
    )

    def __str__(self):
        return self.nome

class Bordas(models.Model):  
    nome = models.CharField(max_length=100) 
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.nome

class Bebidas(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True)  

    def __str__(self):
        return self.nome     
    
class Pedido(models.Model):

    FORMA_PAGAMENTO = [
        ('DINHEIRO', 'Dinheiro'),
        ('CARTAO', 'Cartão de Crédito/Débito'),
        ('PIX', 'Pix'),
    ]

    nome_cliente = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO)
    criado_em = models.DateTimeField(auto_now_add=True)

    bordas = models.ManyToManyField(Bordas, blank=True)
    bebidas = models.ManyToManyField(Bebidas, blank=True)
    
    def __str__(self):
        return f"Pedido #{self.id}"
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        related_name='itens',
        on_delete=models.CASCADE
    )
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    sabores = models.ManyToManyField(Sabores)

    def calcular_total(self):

        if not self.sabores.exists():
            return 0

        categorias = self.sabores.values_list(
            "categoria",
            flat=True
        ).distinct()

        precos = PrecoPizza.objects.filter(
            categoria__in=categorias,
            tamanho=self.tamanho
        ).values_list("preco", flat=True)

        if not precos:
            return 0

        return max(precos)
        
def calcular_total(self):

    total = 0

    # soma pizzas
    for item in self.itens.all():
        total += item.calcular_total()

    # soma bordas
    for borda in self.bordas.all():
        total += borda.preco

    # soma bebidas
    for bebida in self.bebidas.all():
        total += bebida.preco

    return total