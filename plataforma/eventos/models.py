from django.db import models

# Create your models here.
class Eventos(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    organizador = models.CharField(max_length=100)
    usuarios_registrados = models.ManyToManyField('auth.User', related_name='lista_eventos')

    def __str__(self):
        return self.nombre