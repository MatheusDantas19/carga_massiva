from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForms(UserCreationForm):
    first_name = forms.CharField(required=True, label='Primeiro Nome', max_length=20)
    last_name = forms.CharField(required=True, label='Sobrenome', max_length=20)
    username = forms.CharField(required=True, label='Usuario', max_length=20)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data['username']


        try:
            u = User.objects.get(username=username)
        except:
            u = None

        if u is not None:
            raise forms.ValidationError("Já existe um usuário com esse nome")

        return username
