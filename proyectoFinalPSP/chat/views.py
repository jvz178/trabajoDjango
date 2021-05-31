from django.shortcuts import render

def chat(request,especialistaId,usuarioId):

    direccion='ficheros/'+str(usuarioId)+'-'+str(especialistaId)+'.txt'
    fichero = open(direccion,'a+')
    return render(request,"chat.html")