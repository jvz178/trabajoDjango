from django.urls import path, include
from . import views

urlpatterns = [
    path('chat/<int:especialistaId>/<int:usuarioId>',views.chat,name="chat"),
]