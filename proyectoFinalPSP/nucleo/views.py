from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

def inicio(request):
    return render(request,'nucleo/inicio.html')

def logueado(request):
    return render(request,'nucleo/logueado.html')

class updateUser(UpdateView):
    model=User
    fields=['username','password']
    success_url="/logueado"