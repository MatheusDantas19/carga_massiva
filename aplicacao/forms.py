from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ("nome", "sobrenome", "usuario", "senha")

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ("usuario", "senha")

