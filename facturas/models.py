from django.db import models
import pgcrypto
class Factura(models.Model):
    nombre = pgcrypto.EncryptedTextField(cipher='AES', key='factura')
    monto = pgcrypto.EncryptedIntegerField(cipher='AES', key='factura')
    metodo = pgcrypto.EncryptedTextField(cipher='AES', key='factura')
    documento_identidad = pgcrypto.EncryptedTextField(cipher='AES', key='factura')


    def __str__(self):
        return '%s %s' % (self.nombre, self.documento_identidad,self.metodo)