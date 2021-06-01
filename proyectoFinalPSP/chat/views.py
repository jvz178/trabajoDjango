from django.shortcuts import render

crearEscribirFichero=""
direccion=""

def chat(request,especialistaId,usuarioId):
    global crearEscribirFichero, direccion
    direccion='chat/ficheros/'+str(usuarioId)+'-'+str(especialistaId)+'.txt'
    crearEscribirFichero = open(direccion,'a')
    fichero=mostrarMensajes()
    return render(request,"chat.html",{'fichero':fichero})

def guardarMensaje(request, user):
    global crearEscribirFichero, direccion
    mensaje="\n"+str(user)+": "+request.POST.get('comentario','')+" (/)<sig>"
    crearEscribirFichero = open(direccion,'a')
    crearEscribirFichero.write(mensaje)
    fichero=mostrarMensajes()
    return render(request,"chat.html",{'fichero':fichero})

def mostrarMensajes():
    leerFichero = open(direccion,'r')
    fichero=leerFichero.read().split("<sig>")
    return fichero