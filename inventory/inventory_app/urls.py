from django.contrib import admin
from django.conf.urls import url
from inventory_app import views
from django.urls import path

urlpatterns = [
    url(r"^admin/",admin.site.urls),
    path("", views.home, name = "home")
]
