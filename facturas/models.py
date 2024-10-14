from django.db import models

# Create your models here.
from django.db import models

class Factura(models.Model):
    nombre = models.CharField(max_length=100)
    monto = models.FloatField(default =None,null=True,blank=True)
    metodo = models.CharField(max_length=100)
    documento_identidad = models.CharField(max_length=10)


    def __str__(self):
        return '%s %s' % (self.nombre, self.documento_identidad,self.metodo)