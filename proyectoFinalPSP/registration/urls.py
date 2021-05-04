from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('registro/',views.registro,name='registro'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)