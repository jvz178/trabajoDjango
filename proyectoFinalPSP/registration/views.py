from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import FormularioRegistro
from django.urls.base import reverse

def registro(request):
    formulario_registro=FormularioRegistro()

    if request.method=="POST":
        formulario_registro=FormularioRegistro(data=request.POST)
        if formulario_registro.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            return redirect(reverse('login'))
    
    return render(request,'registro.html',{'form':formulario_registro})