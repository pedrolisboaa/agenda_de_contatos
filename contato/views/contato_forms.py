from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contato.forms import ContatoForm
from contato.models import Contato


# Create your views here.


def criar(request):
    acao_formulario = reverse('criar')
     
    if request.method == 'POST':
        formulario = ContatoForm(request.POST)

        context = {
        'formulario': formulario,
        'acao_formulario': acao_formulario,
        }

        if formulario.is_valid():
            contato = formulario.save()
            return redirect('atualizar', id_contato=contato.pk)
        
        return render(request, 'criar.html', context)
         
   
    context = {
        'formulario': ContatoForm(),
        'acao_formulario': acao_formulario,
        }
    
    return render(request, 'criar.html', context)


def atualizar(request, id_contato):
    contato = get_object_or_404(Contato, pk=id_contato, mostrar=True)
    acao_formulario = reverse('atualizar', args=(id_contato,))
     
    if request.method == 'POST':
        formulario = ContatoForm(request.POST, instance=contato)

        context = {
        'formulario': formulario,
        'acao_formulario': acao_formulario,
        }

        if formulario.is_valid():
            contato = formulario.save()
            return redirect('atualizar', id_contato=contato.pk)
        
        return render(request, 'criar.html', context)
         
   
    context = {
        'formulario': ContatoForm(instance=contato),
        'acao_formulario': acao_formulario,
        }
    
    return render(request, 'criar.html', context)


def deletar(request, id_contato):
    contato = get_object_or_404(Contato, pk=id_contato, mostrar=True)
    contato.delete()

    return redirect('index')