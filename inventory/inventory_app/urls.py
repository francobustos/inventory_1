from django.contrib import admin
from django.conf.urls import url
from inventory_app import views
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path("admin/",admin.site.urls),
    path("",views.my_login, name = "login"),
    path("home/", views.Home, name = "home"),
    path('crear_container/',views.crear_container, name = "crear_container"),
    path('editar_container/<int:id>',views.editar_container, name = 'editar_container'),
    path('crear_area/',views.crear_area, name = "crear_area"),
    path('editar_area/<int:id>',views.editar_area, name = 'editar_area'),
    path('crear_objeto/',views.crear_objeto, name = "crear_objeto"),
    path('editar_objeto/<int:id>',views.editar_objeto, name = 'editar_objeto'),
    path('informacion/',views.informacion, name = "informacion"),

]
