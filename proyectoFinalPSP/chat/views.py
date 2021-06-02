from django.shortcuts import render

direccion=""
direccionSinLeer=""
listaMensajes=""
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
    fichero=mensajesSinLeer(fichero)
    return render(request,"chat.html",{'fichero':fichero})

def guardarMensaje(request):
    global direccion, espId, usuId, usuario,rol,direccionSinLeer
    mensaje=str(usuario)+": "+request.POST.get('comentario','')
    abrirFichero = open(direccion,'a')
    abrirFichero.write("\n"+mensaje+"<sig>")
    fichero=mostrarMensajes()
    fichero.append(mensaje+" (Mensaje no leido)")
    reescribeSinLeer()
    return render(request,"chat.html",{'fichero':fichero})


def mostrarMensajes():
    abrirFichero = open(direccion,'a')
    leerFichero = open(direccion,'r')
    fichero=leerFichero.read().split("<sig>")
    return fichero

def mensajesSinLeer(fichero):
    global direccion, espId, usuId, usuario, rol, direccionSinLeer, listaMensajes
    direccionSinLeer="chat/ficheros/sinLeer("+str(usuId)+"-"+str(espId)+").txt"
    abreFichero= open(direccionSinLeer,'a')
    leer=open(direccionSinLeer,'r')
    listaMensajes=leer.read().split(",")
    contador=1
    if(rol=="ROLE_CLI"):
        fichero=verMensajes(listaMensajes,fichero,0, " (Mensaje nuevo)")
        listaMensajes[0]=0
        reescribir=open(direccionSinLeer,'w')
        reescribir.write(str(listaMensajes[0])+","+str(listaMensajes[1]))

        fichero=verMensajes(listaMensajes,fichero,1, " (Mensaje no leido)")
    if(rol=="ROLE_ESP"):
        fichero=verMensajes(listaMensajes,fichero,1, " (Mensaje nuevo)")
        listaMensajes[1]=0
        reescribir=open(direccionSinLeer,'w')
        reescribir.write(str(listaMensajes[0])+","+str(listaMensajes[1]))

        fichero=verMensajes(listaMensajes,fichero,0, " (Mensaje no leido)")

    return fichero

def verMensajes(listaMensajes, fichero, n, texto):
    contador=1
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

def reescribeSinLeer():
    global listaMensajes
    reescribir=open(direccionSinLeer,'w')
    if(rol=="ROLE_CLI"):
        listaMensajes[1]=int(listaMensajes[1])+1
        reescribir.write(str(listaMensajes[0])+","+str(listaMensajes[1]))
    if(rol=="ROLE_ESP"):
        listaMensajes[0]=int(listaMensajes[0])+1
        reescribir.write(str(listaMensajes[0])+","+str(listaMensajes[1]))