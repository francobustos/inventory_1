from django.shortcuts import render,redirect
from inventory_app.models import *
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib import messages


def post_list(request):
    area = Area.objects.all()
    container = Container.objects.all()
    objeto = Objeto.objects.all()
    return render(request, 'index.html', {'area':area, 'container':container, 'objeto':objeto})

<<<<<<< HEAD
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
=======
def objeto(request):
    objeto = Objeto.objects.all()
    return render(request, 'objetos.html',{'objeto':objeto})
>>>>>>> feature
