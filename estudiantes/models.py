from django.db import models
from pgcrypto import fields
from cronograma.models import Cronograma

class Estudiante(models.Model):
    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE, default=None)
    nombre = fields.TextPGPSymmetricKeyField(max_length=50, verbose_name='nombre')
    documento_identidad = fields.TextPGPSymmetricKeyField(max_length=10, verbose_name='documento_identidad')

    def __str__(self):
        return '%s %s' % (self.nombre, self.documento_identidad)