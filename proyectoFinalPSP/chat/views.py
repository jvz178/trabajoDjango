from django.shortcuts import render

def chat(request,especialistaId,usuarioId):

    direccion='chat/ficheros/'+str(usuarioId)+'-'+str(especialistaId)+'.txt'
    crearFichero = open(direccion,'a')
    leerFichero = open(direccion,'r')
    fichero=leerFichero.read()

    return render(request,"chat.html")