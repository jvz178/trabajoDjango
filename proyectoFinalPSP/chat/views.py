from django.shortcuts import render

crearEscribirFichero=""

def chat(request,especialistaId,usuarioId):
    global crearEscribirFichero
    direccion='chat/ficheros/'+str(usuarioId)+'-'+str(especialistaId)+'.txt'
    crearEscribirFichero = open(direccion,'a')
    leerFichero = open(direccion,'r')
    fichero=leerFichero.read().split("<sig>")
    return render(request,"chat.html",{'fichero':fichero})

def mensaje(request):
    global crearEscribirFichero
    print(request)
    return render(request,"chat.html")