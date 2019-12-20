from django.http import HttpResponse
from .models import Pedido
import json

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def detail(request, nombre, email, telefono , direccion , forma_pago , precio):
    detalles = {'nombre': nombre, 'email': email, 'telefono': telefono, 'direccion': direccion, 'forma_pago': forma_pago, 'precio': precio}
    pedidoregistro = Pedido(Nombre=nombre, email=email,telefono=telefono,direccion=direccion,forma_pago=forma_pago,precio=precio)
    pedidoregistro.save()
    return HttpResponse(json.dumps(detalles))
