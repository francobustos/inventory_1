from django.shortcuts import render,redirect
from inventory_app.models import *
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ContainerForm


def post_list(request):
    area = Area.objects.all()
    container = Container.objects.all()
    objeto = Objeto.objects.all()
    return render(request, 'index.html', {'area':area, 'container':container, 'objeto':objeto})

def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('post_list')
        else:
            messages.error(request,'Usuario o contraseña incorrecta')
            return redirect('login')
    else:
        return render(request, 'login.html')

def objeto(request):
    objeto = Objeto.objects.all()
    return render(request, 'objetos.html',{'objeto':objeto})


def crear_container(request):
    if request.method == 'POST':
        container_form = ContainerForm(request.POST)
        if container_form.is_valid():
            container_form.save()
            return redirect('post_list')
    else:
        container_form = ContainerForm()
    return render(request, 'edicion.html', {'form':container_form,'titulo':"Crear container"})
