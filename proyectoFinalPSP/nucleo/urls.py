from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('logueado',views.logueado,name="logueado"),
    path('editarUsuario/<int:pk>',views.updateUser.as_view(), name="editarUsuario"),
    path('listEspecialista',views.EspecialistaListView.as_view(),name="listEspecialista"),
    path('listCliente',views.ClienteListView.as_view(),name="listCliente"),
    path('listCita',views.CitaListView.as_view(),name="listCita"),
    path('citasCliente/<int:idCliente>',views.citasCliente,name="citasCliente"),
    path('deleteCita/<int:pk>',views.CitaDeleteView.as_view(),name="deleteCita"),
    path('updateCita/<int:pk>',views.CitaUpdateView.as_view(),name="updateCita"),
    path('createCita',views.CitaCreateView.as_view(),name="createCita"),
    path('citaInforme/<int:pk>', views.CitaInforme.as_view(),name="citaInforme"),
    path('citaFecha/<int:pk>', views.CitaFecha.as_view(),name="citaFecha"),
    path('chat/<int:especialistaId>',include('chat.urls')),
]
