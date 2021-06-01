from django.shortcuts import render

direccion=""

def chat(request,especialistaId,usuarioId):
    global direccion
    direccion='chat/ficheros/'+str(usuarioId)+'-'+str(especialistaId)+'.txt'
    fichero=mostrarMensajes()
    return render(request,"chat.html",{'fichero':fichero})

def guardarMensaje(request, user):
    global direccion
    mensaje=str(user)+": "+request.POST.get('comentario','')+" (/)"
    abrirFichero = open(direccion,'a')
    abrirFichero.write("\n"+mensaje+"<sig>")
    fichero=mostrarMensajes()
    fichero.append(mensaje)
    return render(request,"chat.html",{'fichero':fichero})

def mostrarMensajes():
    crearEscribirFichero = open(direccion,'a')
    leerFichero = open(direccion,'r')
    fichero=leerFichero.read().split("<sig>")
    return fichero