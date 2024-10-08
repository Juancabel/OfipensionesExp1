# Generated by Django 5.1.1 on 2024-10-08 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cronograma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cuentas', models.IntegerField(blank=True, default=None, null=True)),
                ('monto_total', models.FloatField(blank=True, default=None, null=True)),
                ('periodo_total', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
