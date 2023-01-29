from django.db import models

# Create your models here.


class Registros(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    materia = models.CharField(max_length=50)

    def __str___(self):
        text = "{0} {1}"
        return text.format(self.nombre, self.apellidos)
