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
    return""

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

    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response