from django.db import models

# Create your models here.
class Pedido(models.Model):
    Nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    forma_pago = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)
