from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def cmassiva_index(request):
    print(request.session['user'])
    return render(request, 'c_dashboard.html')

@login_required(login_url='/login')
def cmassiva_gerarcarga():
    pass

@login_required(login_url='/login')
def logoutUser(request):
    logout(request)
    return redirect('login')