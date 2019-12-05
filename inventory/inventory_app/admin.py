from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

##Incompatibilidad con Jet, en exportar, al eligir el tipo de archivo, te lo toma por mas que no te lo muestre

class AreaResource(resources.ModelResource):
    class Meta:
        model = Area

class AreaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre',)
    resource_class = AreaResource

class ContainerResource(resources.ModelResource):
    class Meta:
        model = Container

class ContainerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['ID_profe','nombre']
    list_display = ('nombre','ID_profe','area_de_origen',)
    resource_class = AreaResource

class ObjetoResource(resources.ModelResource):
    class Meta:
        model = Objeto

class ObjetoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['ID_profe','nombre']
    list_display = ('nombre','ID_profe','estado','fecha_entrada',)
    resource_class = ObjetoResource

admin.site.register(Area,AreaAdmin)
admin.site.register(Container,ContainerAdmin)
admin.site.register(Objeto,ObjetoAdmin)
