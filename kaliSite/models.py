from django.db import models

# models são modelos de dados que serão persistido nos banco de dados

class Product(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', blank=True, decimal_places=2, max_digits=7)
    estoque = models.IntegerField('Qtdade em Estoque', default=0)

    def __str__(self):
        return self.nome


class Client(models.Model):
    nome = models.CharField('Nome', max_length=20)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    endereco= models.CharField('Endereço', max_length=100)
    cidade = models.CharField('Cidade', max_length=40)
    estado = models.CharField('Estado', max_length=30)
    email = models.EmailField('Email', max_length=80)
    fone = models.IntegerField('Telefone')

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Order(models.Model):
    cliente = models.CharField('Cliente', max_length=100)
    produto = models.CharField('Produto', max_length=100)
    quantidade = models.IntegerField('Quantidade')
    data = models.DateField('Data')
    email = models.EmailField('Email', max_length=80)
    fone = models.IntegerField('Telefone')

    def __str__(self):
        return f'{self.cliente} - {self.quantidade} de {self.produto}'
