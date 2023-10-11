from django.contrib import admin
from .models import Contato

# Register your models here

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_de_criacao' )
    ordering = '-id',
    #list_filter = ('',)
    search_fields = 'id', 'nome', 'sobrenome', 'telefone', 'email'
    list_per_page = 20
    list_display_links = ('id', 'nome', ) 
    
