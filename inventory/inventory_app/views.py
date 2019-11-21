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

def crear_container(request):
    if request.method == 'POST': #Para ver si la peticion de la pagina quiere enviar algo al servidor
        container_form = ContainerForm(request.POST) #Crea una variable con la peticion que le envia la pagina y lo almacena como un formulario
        if container_form.is_valid(): #Verifica si todos los campos estan bien con respecto a la base de datos
            container_form.save() #Guarda el formulario en la base de datos
            return redirect('post_list') #Redirecciona al index
    else: #Para ver si la peticion de la pagina quiere traer algo del servidor a la pagina
        container_form = ContainerForm() #Crea un formulario vacio
    return render(request, 'edicion.html', {'form':container_form,'titulo':"Crear container"}) #Renderiza la pagina edicion.html y le envia un formulario y un string
