from django.contrib import admin
from .models import *

# Register your models here.

##Incompatibilidad con Jet, en exportar, al eligir el tipo de archivo, te lo toma por mas que no te lo muestre



class AreaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre',)


class ContainerAdmin(admin.ModelAdmin):
    search_fields = ['ID_profe','nombre']
    list_display = ('nombre','ID_profe','area_de_origen',)


class ObjetoAdmin(admin.ModelAdmin):
    search_fields = ['ID_profe','nombre']
    list_display = ('nombre','ID_profe','estado','fecha_entrada',)

admin.site.register(Area,AreaAdmin)
admin.site.register(Container,ContainerAdmin)
admin.site.register(Objeto,ObjetoAdmin)
