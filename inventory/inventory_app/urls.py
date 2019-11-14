from django.contrib import admin
from django.conf.urls import url
from inventory_app import views
from django.urls import path,include

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r"^admin/",admin.site.urls),
    path("",views.my_login, name = "login"),
    path("index/", views.post_list, name = "post_list"),
]
