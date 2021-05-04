from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registro(request):

    form = UserCreationForm()
    context= {'form':form}
    return render(request,'registro.html', context)