from django import forms
from .models import Container, Area, Objeto


class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['ID_profe', 'nombre', 'area_de_origen']


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nombre']


class ObjetoForm(forms.ModelForm):
    class Meta:
        model = Objeto
        fields = ['ID_profe', 'nombre', 'estado', 'caracteristicas',
                  'observaciones', 'fecha_entrada', 'container_de_origen']
        # widgets = { No funcionó
        #     'fecha_entrada': forms.DateInput(),
        # }


class LoginForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
