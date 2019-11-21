from django.db import models

class Area(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

class Container(models.Model):
    ID_profe = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    area_de_origen = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Container'
        verbose_name_plural = 'Containers'


class Objeto(models.Model):
    ID_profe = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    estado = (
        ("N", "Nuevo"),
        ("B","Bueno"),
        ("M", "Malo"),
        ("R","Roto"),
    )
    estado = models.CharField(max_length=1, choices=estado, default="")
    caracteristicas = models.TextField()




    observaciones = models.TextField()
    container_de_origen = models.ForeignKey(Container, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Objeto'
        verbose_name_plural = 'Objetos'


class Prestamo(models.Model):
    fecha_de_prestamo = models.DateTimeField()
    devuelto = models.BooleanField()
    area_de_origen = models.ForeignKey(Area, on_delete=models.CASCADE)
    objeto = models.OneToOneField(Objeto, on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.fecha_de_prestamo

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
