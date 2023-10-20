from django.shortcuts import render, redirect
from contato.models import Contato
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def criar(request):
    context = {
        
    }
    
    return render(request, 'criar.html', context)
