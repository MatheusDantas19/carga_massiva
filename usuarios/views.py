from django.shortcuts import render, redirect
from .forms import UserRegisterForms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your views here.

def cadastrarUsuario(request):
    if request.user.is_authenticated:
        return redirect('cmassiva_dashboard')

    if request.method == "POST":
        form = UserRegisterForms(request.POST)
        if form.is_valid(): #valida o formulairo

            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password1'])
            user.save()

            messages.info(request, "Cadastro realizado com sucesso")

        else:
            return render(request, 'cadastro.html', {'form': form})

    form = UserRegisterForms()
    return render(request, 'cadastro.html', {'form': form})


def loginUsuario(request):
    if request.user.is_authenticated:
        return redirect('cmassiva_dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['user'] = username

            return redirect('cmassiva_dashboard')

        else:
            messages.info(request, "As informações de login estão incorretas")

    form_login = AuthenticationForm()
    return render(request, 'login.html', {'form': form_login})


def index(request):
    if request.user.is_authenticated:
        return redirect('cmassiva_dashboard')

    return redirect('login')
