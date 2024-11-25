from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Adicional(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class Comida(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.nombre} - {self.categoria.nombre}'

class Guarnicion(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()


    def __str__(self):
        return self.nombre

class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()


    def __str__(self):
        return self.nombre

class Postre(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class CafeTe(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()


    def __str__(self):
        return self.nombre


    def __str__(self):
        return self.nombre

from django.db import models

class Mesa(models.Model):
    numero_mesa = models.IntegerField(unique=True)
    sector = models.CharField(max_length=100)

    def __str__(self):
        return f'Mesa {self.numero_mesa} en {self.sector}'


class Pedido_Cliente(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    plato_principal = models.ForeignKey(Comida, on_delete=models.CASCADE)
    adicional_plato_principal = models.ForeignKey(Adicional, related_name='adicionales_plato_cliente', blank=True, null=True, on_delete=models.SET_NULL)
    guarnicion = models.ForeignKey(Guarnicion, on_delete=models.SET_NULL, blank=True, null=True) 
    adicional_guarnicion = models.ForeignKey(Adicional, related_name='adicionales_guarnicion_cliente', blank=True, null=True, on_delete=models.SET_NULL)
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    adicional_bebida = models.ForeignKey(Adicional, related_name='adicionales_bebida_cliente', blank=True, null=True, on_delete=models.SET_NULL)
    postre = models.ForeignKey(Postre, on_delete=models.SET_NULL, blank=True, null=True) 
    adicional_postre = models.ForeignKey(Adicional, related_name='adicionales_postre_cliente', blank=True, null=True, on_delete=models.SET_NULL)
    cafe_te = models.ForeignKey(CafeTe, on_delete=models.SET_NULL, blank=True, null=True)  
    adicional_cafe_te = models.ForeignKey(Adicional, related_name='adicionales_cafe_te_cliente', blank=True, null=True, on_delete=models.SET_NULL)
    fecha_pedido = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Pedido Cliente {self.id} - Mesa {self.mesa.numero_mesa}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Guardar el Pedido_Cliente primero
        self.crear_pedido()  # Llamar al método para crear el Pedido

    def crear_pedido(self):
        # Crear un nuevo objeto Pedido basado en Pedido_Cliente
        pedido = Pedido(
            mesa=self.mesa,
            plato_principal=self.plato_principal,
            adicional_plato_principal=self.adicional_plato_principal,
            guarnicion=self.guarnicion,
            adicional_guarnicion=self.adicional_guarnicion,
            bebida=self.bebida,
            adicional_bebida=self.adicional_bebida,
            postre=self.postre,
            adicional_postre=self.adicional_postre,
            cafe_te=self.cafe_te,
            adicional_cafe_te=self.adicional_cafe_te,
            fecha_pedido=self.fecha_pedido
        )
        pedido.save()  # Guardar el nuevo Pedido

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    plato_principal = models.ForeignKey(Comida, on_delete=models.CASCADE)
    adicional_plato_principal = models.ForeignKey(Adicional, related_name='adicionales_plato', blank=True, null=True, on_delete=models.SET_NULL)
    guarnicion = models.ForeignKey(Guarnicion, on_delete=models.SET_NULL, blank=True, null=True) 
    adicional_guarnicion = models.ForeignKey(Adicional, related_name='adicionales_guarnicion', blank=True, null=True, on_delete=models.SET_NULL)
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    adicional_bebida = models.ForeignKey(Adicional, related_name='adicionales_bebida', blank=True, null=True, on_delete=models.SET_NULL)
    postre = models.ForeignKey(Postre, on_delete=models.SET_NULL, blank=True, null=True) 
    adicional_postre = models.ForeignKey(Adicional, related_name='adicionales_postre', blank=True, null=True, on_delete=models.SET_NULL)
    cafe_te = models.ForeignKey(CafeTe, on_delete=models.SET_NULL, blank=True, null=True)  
    adicional_cafe_te = models.ForeignKey(Adicional, related_name='adicionales_cafe_te', blank=True, null=True, on_delete=models.SET_NULL)
    fecha_pedido = models.DateTimeField(default=timezone.now)
    total = models.FloatField(default=0.0)
    entregado = models.BooleanField(default=False)

    def calcular_total(self):
        # Sumar el precio de los productos
        total = self.plato_principal.precio + \
                (self.guarnicion.precio if self.guarnicion else 0) + \
                self.bebida.precio + \
                (self.postre.precio if self.postre else 0) + \
                (self.cafe_te.precio if self.cafe_te else 0)

        # Sumar los adicionales seleccionados para cada producto
        if self.adicional_plato_principal:
            total += self.adicional_plato_principal.precio
        if self.adicional_guarnicion:
            total += self.adicional_guarnicion.precio
        if self.adicional_bebida:
            total += self.adicional_bebida.precio
        if self.adicional_postre:
            total += self.adicional_postre.precio
        if self.adicional_cafe_te:
            total += self.adicional_cafe_te.precio

        return total

    def save(self, *args, **kwargs):
        # Calcula el total automáticamente antes de guardar
        self.total = self.calcular_total()
        super().save(*args, **kwargs)

    def __str__(self):
        estado_entrega = "Entregado" if self.entregado else "No entregado"
        return f'Pedido en Mesa {self.mesa.numero_mesa} - Total: {self.total} - {estado_entrega}'

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Mensaje de { self.nombre} - {self.email}'
