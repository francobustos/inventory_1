from django import forms
from .models import Container,Area

class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['ID_profe','nombre','area_de_origen']

class AreaForm(forms.ModelForm):
	class Meta:
		model = Area
		fields = ['nombre']
