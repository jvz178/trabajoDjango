from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('logueado',views.logueado,name="logueado"),
    path('editarUsuario/<int:pk>',views.updateUser.as_view(), name="editarUsuario"),
]
