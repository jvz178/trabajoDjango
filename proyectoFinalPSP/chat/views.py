from django.shortcuts import render

direccion=""
espId=""
usuId=""
usuario=""
rol=""

def chat(request,especialistaId,usuarioId,user,role):
    global direccion, espId, usuId, usuario, rol
    espId=especialistaId
    usuId=usuarioId
    usuario=user
    rol=role
    direccion='chat/ficheros/'+str(usuarioId)+'-'+str(especialistaId)+'.txt'
    fichero=mostrarMensajes()
    return fichero

def chatReciente(request,especialistaId,usuarioId,user,role):
    fichero=chat(request,especialistaId,usuarioId,user,role)
    if(len(fichero)>8):
        fichero=obtenerUltimosMensajes(fichero,8)
    return render(request,"chat.html",{'fichero':fichero})

def historialChat(request):
    fichero=chat(request,espId,usuId,usuario,rol)
    return render(request,"historialChat.html",{'fichero':fichero}) 

def guardarMensaje(request):
    global direccion, espId, usuId, usuario,rol,direccionSinLeer
    mensaje=str(usuario)+": "+request.POST.get('comentario','')
    abrirFichero = open(direccion,'a')
    abrirFichero.write("\n"+mensaje+"<sig>")
    fichero=mostrarMensajes()
    fichero.append(mensaje)
    return render(request,"chat.html",{'fichero':fichero})


def obtenerUltimosMensajes(fichero,n):
    contador=n
    contador2=0
    nuevoFichero=[""]*n
    while(contador>0):
        nuevoFichero[contador2]=fichero[len(fichero)-contador]
        contador=contador-1
        contador2=contador2+1
    return nuevoFichero

def mostrarMensajes():
    abrirFichero = open(direccion,'a')
    leerFichero = open(direccion,'r')
    fichero=leerFichero.read().split("<sig>")
    return fichero

def verMensajes(fichero, n, texto):
    global listaMensajes
    contador=1
    print("DATO: "+listaMensajes[n])
    if(int(listaMensajes[n])>0):
            contadorMensajes=listaMensajes[n]
            while(int(contadorMensajes)>0):
                if(fichero[len(fichero)-contador] != ""):
                    print("INFO: "+fichero[len(fichero)-contador][:len(usuario)+1])
                    if(fichero[len(fichero)-contador][:len(usuario)+1]!=usuario):
                        print("ENTRA1")
                        fichero[len(fichero)-contador]=fichero[len(fichero)-contador]+texto
                        contadorMensajes=int(contadorMensajes)-1
                    if(fichero[len(fichero)-contador][:len(usuario)+1]==usuario):
                        print("ENTRA2")
                        fichero[len(fichero)-contador]=fichero[len(fichero)-contador]+texto
                        contadorMensajes=int(contadorMensajes)-1
                contador=int(contador)+1
    return fichero