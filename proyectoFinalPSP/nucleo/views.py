from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .models import Especialista
from .forms import CitaForm
from django.urls import reverse

def inicio(request):
    return render(request,'nucleo/inicio.html')

def logueado(request):
    return render(request,'nucleo/logueado.html')

def cita(request):
    cita_form=CitaForm()
    if request.method=="POST":
        cita_form=CitaForm(data=request.POST)
        if cita_form.is_valid():
            cita_form.save()
    return render(request,"nucleo/cita.html",{'form':cita_form})

class updateUser(UpdateView):
    model=User
    fields=['username','password']
    success_url="/logueado"

class EspecialistaListView(ListView):
    model=Especialista