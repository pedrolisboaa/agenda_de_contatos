from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    imagem = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )
    class Meta:
        model = Contato
        fields = ('nome', 'sobrenome', 'telefone', 'email', 'descricao', 'categoria', 'imagem')

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'classe-a classe-b',
                    'placeholder': 'Informe seu nome',
                }
            )
        }