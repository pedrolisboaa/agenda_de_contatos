from django import forms
from .models import Contato
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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

class FormularioDeRegistro(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValueError('Já existe esse e-mail', code='invalid')
            )
            
        return email