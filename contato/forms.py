from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ('nome', 'sobrenome', 'telefone', 'email', 'descricao', 'categoria')

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'classe-a classe-b',
                    'placeholder': 'Informe seu nome',
                }
            )
        }