from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from django.contrib.auth.models import User
from .models import Especialista, Cita, Cliente
from .forms import CitaForm, InformeForm
from django.urls import reverse
from django.http.response import Http404
from django.http import HttpResponse
from datetime import datetime
from datetime import date
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from reportlab.platypus import TableStyle,Table
from reportlab.lib import colors
from reportlab.lib.units import cm

fechaHora = datetime.now()
#fecha=fechaHora.strftime('%d/%m/%Y')
fecha=date.today()

def inicio(request):
    return render(request,'nucleo/inicio.html')

def logueado(request):
    return render(request,'nucleo/logueado.html')

def fechasPDF(request):
    return render(request,'nucleo/fechasPDF.html')

def generarPDF (request):
    print("HOLAAAAAA: "+request.POST.get('inicio',''))
    print("HOLAAAAAAAAAAAA: "+request.POST.get('final',''))
    return render(request,'pdfCliente')

def cita(request):
    cita_form=CitaForm()
    if request.method=="POST":        
        cita_form=CitaForm(data=request.POST)
        if cita_form.is_valid():
            realizada=request.POST.get('realizada',False)
            cita_form.save()
    return render(request,"nucleo/cita.html",{'form':cita_form})

def citasCliente(request,idCliente):
    try:
        ct=Cita.objects.get(idCliente=idCliente)
    except ct.DoesNotExist:
        raise Http404('Este cliente no tiene citas')
    context={'ct':ct}
    return render(request,"nucleo/citasCliente.html",context)

class updateUser(UpdateView):
    model=User
    fields=['username','password']
    success_url="/logueado"

class EspecialistaListView(ListView):
    model=Especialista

class CitaCreateView(CreateView):
    model=Cita
    fields=['fecha','idCliente','idEspecialista','informe','realizada']
    success_url="/listEspecialista"

class ClienteListView(ListView):
    model=Cliente

class CitaListView(ListView):
    model=Cita

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fecha"] = fecha
        return context
    

class CitaDeleteView(DeleteView):
    model=Cita
    success_url="/listCita"

class CitaUpdateView(UpdateView):
    model=Cita
    fields=['fecha','idEspecialista']
    success_url="/listCita"

class CitaInforme(UpdateView):
    model=Cita
    form_class=InformeForm
    template_name="nucleo/cita_form.html"
    success_url="/listCita"

class CitaFecha(UpdateView):
    model=Cita
    fields=['fecha']
    template_name="nucleo/cita_form.html"
    success_url="/listCita"

class pdfCliente(View):

    def cabecera(self,pdf):
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u"Yo te ayudo")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"Juntos superamos el COVID-19")

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y=600
        self.tablaCliente(pdf,y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
    
    def tablaCliente(self,pdf,y):
        encabezados = ('DNI', 'Nombre', 'Apellidos', 'Direccion', 'Fecha de nacimiento','foto','Id')
        detalles = [(Cliente.dni, Cliente.nombre, Cliente.apellidos, Cliente.direccion,Cliente.fechaNacimiento,Cliente.foto,Cliente.idUsuario) for Cliente in Cliente.objects.all()]
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 5 * cm, 5 * cm, 5 * cm, 5 * cm, 5 * cm])
        detalle_orden.setStyle(TableStyle(
            [
                ('ALIGN',(0,0),(3,0),'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60,y)