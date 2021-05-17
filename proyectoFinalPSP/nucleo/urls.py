from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('logueado',views.logueado,name="logueado"),
    path('editarUsuario/<int:pk>',views.updateUser.as_view(), name="editarUsuario"),
    path('listEspecialista',views.EspecialistaListView.as_view(),name="listEspecialista"),
    path('listCita',views.CitaListView.as_view(),name="listCita"),
    path('cita',views.cita,name="cita"),
    path('deleteCita/<int:pk>',views.CitaDeleteView.as_view(),name="deleteCita"),
    path('updateCita/<int:pk>',views.CitaUpdateView.as_view(),name="updateCita"),
]
