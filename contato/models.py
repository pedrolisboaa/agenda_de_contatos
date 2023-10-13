from django.db import models
from django.utils import timezone
# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    data_de_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True) 
    mostrar = models.BooleanField(default=True)
    imagem = models.ImageField(blank=True, upload_to='imagens/%Y/%m')
    


    def __str__(self):
        return self.nome