from django.db import models
import pgcrypto
from cronograma.models import Cronograma

class Estudiante(models.Model):
    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE, default=None)
    nombre = pgcrypto.EncryptedTextField(cipher='AES', key='estudiante')
    documento_identidad = pgcrypto.EncryptedTextField(cipher='AES', key='estudiante')

    def __str__(self):
        return '%s %s' % (self.nombre, self.documento_identidad)