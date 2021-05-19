from django.contrib import admin
from .models import Cliente, Especialista, Cita, Mensaje, Role

admin.site.register(Role)
admin.site.register(Cliente)
admin.site.register(Especialista)
admin.site.register(Cita)
admin.site.register(Mensaje)