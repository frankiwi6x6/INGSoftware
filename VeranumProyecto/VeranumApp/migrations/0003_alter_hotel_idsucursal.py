# Generated by Django 4.2.1 on 2023-06-12 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VeranumApp', '0002_tipohabitacion_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='idSucursal',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
