from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url='/login')
def listarUsuario(request):
    
    return render(request, 'listar.html', {'dados': request.session['usuario']})

def cadastrarUsuario(request):
    list(messages.get_messages(request))

    if request.user.is_authenticated:
        return redirect('listar_usuario')

    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Cadastro realizado com sucesso")

    form = UsuarioForm()
    return render(request, 'cadastro.html', {'form': form })

def loginUsuario(request):
    list(messages.get_messages(request))

    if request.user.is_authenticated:
        return redirect('listar_usuario')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['usuario'] = username

            return redirect('listar_usuario')
        else: 
            messages.info(request, "As informações de login estão incorretas")

    form_login = AuthenticationForm()
    return render(request, 'login.html',  {'form': form_login})
    
@login_required(login_url='/login')
def logoutUsuario(request):
    logout(request)
    del request.session['usuario']
    return redirect('login')

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', {'dados': request.session['usuario']})

    else:
        return redirect('login')