from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome
    
    

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    data_de_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True) 
    mostrar = models.BooleanField(default=True)
    imagem = models.ImageField(blank=True, upload_to='imagens/%Y/%m')
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True)
    dono = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True)
    
    class Meta:
        verbose_name = 'Cantato'
        verbose_name_plural = 'Contatos'
    
    def __str__(self):
        return self.nome