from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UploadAlunoRel, UploadCarga
from django.contrib import messages
import os
from .functions_pandas import gerarCargaMassiva, gerarCargaMassivaGenero, dividirCarga, juntarCarga

from django.views.static import serve


# Create your views here.


@login_required(login_url='/login')
def cmassiva_index(request):
    path = "c_massiva/uploads/"+request.session['user']+'/'

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)

    return render(request, 'c_dashboard.html')

@login_required(login_url='/login')
def cmassiva_gerarcarga(request):
    form = UploadAlunoRel()

    if request.method == 'POST':
        form = UploadAlunoRel(request.POST, request.FILES)
        if form.is_valid():

            csv_file = request.FILES['file']
            choice = request.POST['choice']
            user = request.session['user']

            if(request.POST['submit'] == 'gc'):
                status = gerarCargaMassiva(csv_file, user, choice)
            else:
                status = gerarCargaMassivaGenero(csv_file, user, choice)

            print(status)
            if status:
                filepath = 'c_massiva/uploads/'+user+'/cargaGerada.csv'
                return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

    return render(request,'c_gerador.html', {'form':form})

def cmassiva_opcoes(request):
    form = UploadCarga()

    if request.method == 'POST':
        form = UploadCarga(request.POST, request.FILES)

        if form.is_valid():
            user = request.session['user']

            if request.POST['submit'] == 'dividir':
                csv_file = request.FILES['file']
                status = dividirCarga(csv_file, user)
                if status:
                    return render(request,'c_response.html')

                messages.error("Erro ao ler o arquivo")

            elif request.POST['submit'] == 'juntar':
                files = request.FILES.getlist("file")
                status = juntarCarga(files, user)

                if status:
                    print("Carga combinada")
                    filepath = 'c_massiva/uploads/'+user+'/carga_combinada.csv'
                    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

                messages.error("Erro ao ler o arquivo")

            else:
                csv_file = request.FILES['file']
                pass


    return render(request, 'c_opcoes.html', {'form':form})


def cmassiva_response(request):
    return render(request,'c_response.html')

@login_required(login_url='/login')
def logoutUser(request):
    logout(request)
    return redirect('login')