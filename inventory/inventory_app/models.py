from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=60)
    admin = models.BooleanField()

    def __str__(self):
        return self.nombreS

class Area(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Container(models.Model):
    ID_profe = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    area_de_origen = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Objeto(models.Model):
    ID_profe = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    estado = (
        ("NV", "Nuevo"),
        ("BN","Bueno"),
        ("ML", "Malo"),
        ("RT","Roto"),
    )
    estado = models.CharField(max_length=1, choices=estado, default="")
    caracteristicas = models.TextField()
    observaciones = models.TextField()
    conteiner_de_origen = models.ForeignKey(Container, on_delete=models.CASCADE)

    def __Str__(self):
        return self.nombre

class Prestamo(models.Model):
    fecha_de_prestamo = models.DateTimeField()
    devuelto = models.BooleanField()
    area_de_origen = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha_de_prestamo
