from django.db import models
import time

class Area(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

class Container(models.Model):
    ID_profe = models.CharField(max_length=30, blank = True)
    nombre = models.CharField(max_length=30)
    area_de_origen = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return "{0},{1},{2}".format(self.area_de_origen.nombre, self.nombre,self.ID_profe)

    class Meta:
        verbose_name = 'Container'
        verbose_name_plural = 'Containers'


class Objeto(models.Model):
    ID_profe = models.CharField(max_length=30, blank = True)
    nombre = models.CharField(max_length=30)
    estado = (
        ("N", "Nuevo"),
        ("B","Bueno"),
        ("M", "Malo"),
        ("R","Roto"),
    )
    estado = models.CharField(max_length=1, choices=estado, default="")
    caracteristicas = models.TextField(blank = True, null = True)
    observaciones = models.TextField(blank = True, null = True)
    fecha_entrada = models.DateField(blank = True, null = True, default = (str(time.strftime("%m/%d/%y"))))
    container_de_origen = models.ForeignKey(Container, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Objeto'
        verbose_name_plural = 'Objetos'
