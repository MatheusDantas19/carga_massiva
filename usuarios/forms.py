from django.contrib.auth import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("first_name", "last_name", "username", "password1", "password2")

# class UserCreationForm(forms.UserCreationForm):
#     class Meta(forms.UserCreationForm.Meta):
#         model = Usuario

# class UserChangeForm(forms.UserChangeForm):
#     class Meta(forms.UserChangeForm.Meta):
#         model = Usuario
        
# from .models import Usuario

# class UsuarioForm(forms.ModelForm):
#     senha = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = Usuario
#         fields = ("nome", "sobrenome", "usuario", "senha")

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ("usuario", "senha")

