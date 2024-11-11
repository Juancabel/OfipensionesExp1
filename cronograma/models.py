from django.db import models
import pgcrypto

# Create your models here.

class Cronograma(models.Model):
    num_cuentas = pgcrypto.EncryptedIntegerField(cipher='AES', key='cronograma')
    monto_total = pgcrypto.EncryptedDecimalField(cipher='AES', key='cronograma')
    periodo_total = pgcrypto.EncryptedIntegerField(cipher='AES', key='cronograma')

    def __str__(self):
        return '%s %s %s' % (self.num_cuentas, self.monto_total, self.periodo_total)