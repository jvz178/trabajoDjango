from django.urls import path, include
from . import views

urlpatterns = [
    path('chat/<int:usuarioId>/<int:especialistaId>/<str:user>/<str:role>',views.chat,name="chat"),
    path('guardarMensaje',views.guardarMensaje,name="guardarMensaje"),
]