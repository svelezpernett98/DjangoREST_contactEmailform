from django.db import models
from datetime import datetime

# Create your models here.

class Cliente(models.Model):
    idCliente = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=40)

    # def nombreCliente(self):
    #     txt = "{0} {1}"
    #     return txt.format(self.nombre, self.apellido)

    # def __str__(self):
    #     txt = "{0}, cedula: {1}"
    #     return txt.format(self.nombreCliente(), self.idCliente)

    def __str__(self):
        return self.nombre + ", CC" + self.idCliente

class Producto(models.Model):
    idProducto = models.CharField(max_length=10, primary_key=True)
    nombreProducto = models.CharField(max_length=30)
    valorProducto = models.IntegerField()

    def __str__(self):
        txt = "{0} con valor por unidad: {1}"
        return txt.format(self.nombreProducto, self.valorProducto)

class Tienda(models.Model):
    idTienda = models.CharField(max_length=3, primary_key=True)
    ciudad = models.CharField(max_length=15)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        txt = "Maaji {0}"
        return txt.format(self.ciudad)

class Factura(models.Model):
    idFactura = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad_producto = models.IntegerField()
    idCliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    idTienda = models.ForeignKey(Tienda, null=False, blank=False, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)

    objetoProducto = Producto()
    objetoTienda = Tienda()

    def __str__(self):
        fechaFactura = self.fecha.strftime("%Y/%m/%D, %H:%M:%S")
        txt = "{0},{1},{2},{3},{4},{5}"
        return txt.format(self.idFactura, self.fecha, self.objetoProducto.nombreProducto, self.cantidad_producto, self.idCliente, self.objetoTienda.ciudad)
