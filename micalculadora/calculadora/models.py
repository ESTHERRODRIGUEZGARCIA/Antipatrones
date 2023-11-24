from django.db import models

# Create your models here.
# calculadora/models.py

from django.db import models

class HistorialOperaciones(models.Model):
    operacion = models.CharField(max_length=20)
    resultado = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)
