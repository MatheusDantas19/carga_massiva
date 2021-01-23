from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def listarUsuario(request):
    usuario = Usuario.objects.all()
    return render(request, 'listar.html', {'dados': usuario})

def inserirUsuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        print(request.POST['usuario'])
        if form.is_valid():
            user = User.objects.create_user(request.POST['usuario'], request.POST['usuario']+"@gmail.com" ,request.POST['senha'])
            user.last_name = request.POST['sobrenome']
            user.save()

            u = User.objects.get(username=request.POST['usuario'])
            u.last_name = '1233123'
            u.set_password('oioioio')
            u.save()

            form.save()
            return redirect('listar_usuario')
    else: 
        form = UsuarioForm()
    return render(request, 'form_usuario.html', {'form': form })

def login(request):
    if request.method == 'POST':
        # form = LoginForm(request.POST)
        username = request.POST['usuario']
        password = request.POST['senha']
        print(request.POST)
        
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            return redirect('listar_usuario')
        else: 
            return redirect('login')
    else:
        form_login = LoginForm()
        return render(request, 'login.html',  {'form': form_login})
    