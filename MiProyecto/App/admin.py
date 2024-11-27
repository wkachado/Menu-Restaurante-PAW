from django.contrib import admin
from .models import *

admin.site.register(Categoria)
admin.site.register(Comida)
admin.site.register(Guarnicion)
admin.site.register(Bebida)
admin.site.register(Postre)
admin.site.register(CafeTe)
admin.site.register(Mesa)
admin.site.register(Pedido)
admin.site.register(Adicional)
admin.site.register(Pedido_Cliente)