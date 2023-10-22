from typing import Any
from django.shortcuts import render, redirect
from contato.models import Contato
from contato.forms import ContatoForm


# Create your views here.


def criar(request):
     
    if request.method == 'POST':
        context = {
        'formulario': ContatoForm(request.POST)
    }
        
        return render(request, 'criar.html', context)
         
   
    context = {
        'formulario': ContatoForm()
    }
    
    return render(request, 'criar.html', context)
