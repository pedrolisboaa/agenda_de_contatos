from django.shortcuts import render, redirect
from contato.models import Contato
from django.http import Http404
from django.db.models import Q

# Create your views here.

def index(request):
    contatos = Contato.objects.filter(mostrar=True).order_by('-id')
    context = {
        #'contatos': contatos,
        'contatos': contatos
    }
    
    return render(request, 'index.html', context)


def buscar(request):
    
    valor_buscar = request.GET.get('q', '').strip()
    if valor_buscar == '':
        return(redirect('index'))
    
    contatos = Contato.objects \
    .filter(mostrar=True) \
    .filter(
        Q(nome__icontains=valor_buscar) |
        Q(telefone__icontains=valor_buscar) |
        Q(nome__icontains=valor_buscar) |
        Q(sobrenome__icontains=valor_buscar)) \
    .order_by('id')

    context = {
        'contatos': contatos
    }
    
    return render(request, 'index.html', context)


def contato_unico(request, id_contato):

    contato_u = Contato.objects.filter(pk=id_contato, mostrar=True).first()

    if contato_u is None:
        raise Http404()
    
    context = {
        'contato': contato_u
    }

    return render(request, 'contato_unico.html', context)


