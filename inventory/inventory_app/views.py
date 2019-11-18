from django.shortcuts import render
from inventory_app.models import *
from django.utils import timezone

def post_list(request):
    area = Area.objects.all()
    container = Container.objects.all()
    objeto = Objeto.objects.all()
    return render(request, 'index.html', {'area':area, 'container':container, 'objeto':objeto})

def area(request):
	area = Area.objects.all()
	container = Container.objects.all()
	return render(request, 'areas.html', {'area':area, 'container':container })
