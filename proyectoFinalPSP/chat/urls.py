from django.urls import path, include
from . import views

urlpatterns = [
    path('chat/<int:usuarioId>/<int:especialistaId>/<str:user>/<str:role>',views.chatReciente,name="chatReciente"),
    path('historialChat',views.historialChat,name="historialChat"), 
    path('guardarMensaje',views.guardarMensaje,name="guardarMensaje"),
]