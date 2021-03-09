from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UploadCarga
from django.core.files.storage import FileSystemStorage
import os
from .functions_pandas import gerarCargaMassiva

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
    form = UploadCarga()

    if request.method == 'POST':
        form = UploadCarga(request.POST,request.FILES)
        if form.is_valid():
            print("Valido")

            csv_file = request.FILES['file']
            status = gerarCargaMassiva(csv_file, request.session['user'])

            if status:
                pass


    return render(request,'c_gerador.html', {'form':form})

@login_required(login_url='/login')
def logoutUser(request):
    logout(request)
    return redirect('login')