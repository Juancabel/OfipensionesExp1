from django.db import models
from pgcrypto import fields


# Create your models here.

class Cronograma(models.Model):
    num_cuentas = fields.IntegerPGPSymmetricKeyField(default =None,null=True,blank=True, verbose_name='num_cuentas')
    monto = fields.FloatPGPSymmetricKeyField(default =None,null=True,blank=True, verbose_name='monto')
    periodo_total = fields.IntegerPGPSymmetricKeyField(default =None,null=True,blank=True, verbose_name='periodo_total')

    def __str__(self):
        return '%s %s %s' % (self.num_cuentas, self.monto_total, self.periodo_total)