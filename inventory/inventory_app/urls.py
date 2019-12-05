from django.contrib import admin
from django.conf.urls import url
from inventory_app import views
from django.urls import path, include
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path("accounts/login/",views.my_login, name = "login"),
    path("", views.Home, name = "home"),
    path("logout/",logout_then_login, name = "logout"),
    path('crear_container/',views.crear_container, name = "crear_container"),
    path('editar_container/<int:id>',views.editar_container, name = 'editar_container'),
    path('crear_area/',views.crear_area, name = "crear_area"),
    path('editar_area/<int:id>',views.editar_area, name = 'editar_area'),
    path('crear_objeto/',views.crear_objeto, name = "crear_objeto"),
    path('editar_objeto/<int:id>',views.editar_objeto, name = 'editar_objeto'),
    path('informacion/',views.post_list, name = "informacion"),
    path('eliminar_area/<int:id>',views.eliminar_area , name = 'eliminar_area'),
    path('eliminar_container/<int:id>',views.eliminar_container , name = 'eliminar_container'),
    path('eliminar_objeto/<int:id>',views.eliminar_objeto , name = 'eliminar_objeto'),
    path('objetos/', views.pdfInfo, name='pdf_informacion'),
]
