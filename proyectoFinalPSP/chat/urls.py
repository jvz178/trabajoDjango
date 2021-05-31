from django.urls import path, include
from . import views

urlpatterns = [
    path('chat/<int:usuarioId>/<int:especialistaId>',views.chat,name="chat"),
    path('mensaje',views.mensaje,name="mensaje"),
]