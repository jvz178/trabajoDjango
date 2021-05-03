from django.db import models

class Usuario(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Cliente(models.Model):
    dni=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    fechaNacimiento=models.DateField()
    foto=models.CharField(max_length=100)
    idUsuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Especialista(models.Model):
    dni=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    fechaNacimiento=models.DateField()
    foto=models.CharField(max_length=100)
    biografia=models.CharField(max_length=255)
    idUsuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Cita(models.Model):
    fecha=models.DateField()
    idCliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    idEspecialista=models.ForeignKey(Especialista,on_delete=models.CASCADE)
    informe=models.TextField()
    realizada=models.BooleanField()

class Mensaje(models.Model):
    idEmisor=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    idReceptor=models.ForeignKey(Usuario,related_name='%(class)s_requests_created',on_delete=models.CASCADE)
    fecha=models.DateField()
    asunto=models.CharField(max_length=50)
    texto=models.TextField()
    leido=models.BooleanField()