from django.shortcuts import render,redirect
from inventory_app.models import *
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ContainerForm, AreaForm, ObjetoForm
from django.contrib.auth.decorators import login_required

#login_required(login_url="login")
def Home(request):
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
            return redirect('home')
        else:
            messages.error(request,'Usuario o contraseña incorrecta')
            return redirect('login')
    else:
        return render(request, 'login.html')

#@login_required(login_url="login")
def crear_container(request):
    if request.method == 'POST': #Para ver si la peticion de la pagina quiere enviar algo al servidor
        container_form = ContainerForm(request.POST) #Crea una variable con la peticion que le envia la pagina y lo almacena como un formulario
        if container_form.is_valid(): #Verifica si todos los campos estan bien con respecto a la base de datos
            container_form.save() #Guarda el formulario en la base de datos
            return redirect('home') #Redirecciona al index
    if request.method == 'GET': #Para ver si la peticion de la pagina quiere traer algo del servidor a la pagina
        container_form = ContainerForm() #Crea un formulario vacio
    return render(request, 'edicion.html', {'form':container_form,'titulo':"Crear container"}) #Renderiza la pagina edicion.html y le envia un formulario y un string


#@login_required(login_url="login")
def editar_container(request, id):
    container = Container.objects.get(id = id)
    if request.method == 'GET':
        container_form = ContainerForm(instance = container)
    if request.method == 'POST':
        container_form = ContainerForm(request.POST, instance = container)
        if container_form.is_valid():
            container_form.save()
        return redirect('home')
    return render(request, 'edicion.html', {'form': container_form, 'titulo': 'Editar Container'})

#@login_required(login_url="login")
def crear_area(request):
    if request.method == 'POST':
        area_form = AreaForm(request.POST)
        if area_form.is_valid():
            area_form.save()
            return redirect('home')
    if request.method == 'GET':
        area_form = AreaForm()
    return render(request, 'edicion.html', {'form':area_form,'titulo':"Crear Area"})

#@login_required(login_url="login")
def editar_area(request, id):
    area = Area.objects.get(id = id)
    if request.method == 'GET':
        area_form = AreaForm(instance = area)
    if request.method == 'POST':
        area_form = AreaForm(request.POST, instance = area)
        if area_form.is_valid():
            area_form.save()
        return redirect('home')
    return render(request, 'edicion.html', {'form': area_form, 'titulo': 'Editar Area'})

#@login_required(login_url="login")
def crear_objeto(request):
    if request.method == 'POST':
        objeto_form = ObjetoForm(request.POST)
        if objeto_form.is_valid():
            objeto_form.save()
            return redirect('home')
    if request.method == 'GET':
        objeto_form = ObjetoForm()
    return render(request, 'edicion.html', {'form':objeto_form,'titulo':"Crear Objeto"})

#@login_required(login_url="login")
def editar_objeto(request, id):
    objeto = objeto.objects.get(id = id)
    if request.method == 'GET':
        objeto_form = ObjetoForm(instance = objeto)
    if request.method == 'POST':
        objeto_form = ObjetoForm(request.POST, instance = objeto)
        if objeto_form.is_valid():
            objeto_form.save()
        return redirect('home')
    return render(request, 'edicion.html', {'form': objeto_form, 'titulo': 'Editar Objeto'})

def post_list(request):
    lista = Objetos.objects.all()
    return render(request,'info.html',{'lista':lista})
