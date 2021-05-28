from django.shortcuts import render

def chat(request,especialistaId):
    fichero = open('ficheros/{{user.id}}-'+especialistaId,'r')
    return render(request,"chat.html")
