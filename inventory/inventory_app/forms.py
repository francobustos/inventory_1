from django import forms
from .models import Container

class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['ID_profe','nombre','area_de_origen']
