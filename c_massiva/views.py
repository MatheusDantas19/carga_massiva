from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UploadAlunoRel, UploadCarga
from django.core.files.storage import FileSystemStorage
import os
from .functions_pandas import gerarCargaMassiva, gerarCargaMassivaGenero, dividirCarga

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
        print(form)
        if form.is_valid():
            csv_file = request.FILES['file']
            user = request.session['user']

            if request.POST['submit'] == 'dividir':
                status = dividirCarga(csv_file, user)

                if status:
                    print("OK")

                print("Error")

            elif request.POST['submit'] == 'Checkup':
                pass
            else:
                pass



    return render(request, 'c_opcoes.html', {'form':form})


def cmassiva_response(request):
    return render(request,'c_response.html')

@login_required(login_url='/login')
def logoutUser(request):
    logout(request)
    return redirect('login')