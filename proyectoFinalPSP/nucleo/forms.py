from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model=Cita
        fields=['fecha','idCliente','idEspecialista','informe','realizada']

class InformeForm(forms.ModelForm):
    class Meta:
        model=Cita
        fields=['informe','realizada']
        widgets={
            'informe':forms.Textarea(attrs={'class':'form-control'}),
        }
