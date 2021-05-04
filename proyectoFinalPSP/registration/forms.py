from django import forms

class FormularioRegistro(forms.Form):
    username=forms.CharField(label="Nombre", required=True)
    password=forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput)