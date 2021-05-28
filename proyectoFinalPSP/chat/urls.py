from django.urls import path, include
from . import views

urlpatterns = [
    path('chat/<int:especialistaId>',views.chat,name="chat"),
]