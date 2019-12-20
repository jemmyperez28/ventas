from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'email', 'telefono', 'direccion', 'forma_pago', 'precio')

admin.site.register(Pedido, PedidoAdmin)
admin.site.unregister(Group)