from django.shortcuts import render
from contato.forms import FormularioDeRegistro

def registro(request):
    formulario = FormularioDeRegistro
    
    if request.method == 'POST':
        formulario = FormularioDeRegistro(request.POST)
        
        if formulario.is_valid():
            formulario.save()
    
    context = {
        'formulario': formulario,
    }
    
    return render(request, 'registro.html', context)