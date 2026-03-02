from django.db import models

# Criando o modelo para pizza 

class Pizza(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
class Sabores(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Acompanhamentos(models.Model):  
    nome = models.CharField(max_length=100) 
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.nome
