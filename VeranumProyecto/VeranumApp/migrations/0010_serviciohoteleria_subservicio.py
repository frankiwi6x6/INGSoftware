# Generated by Django 4.2.1 on 2023-06-13 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VeranumApp', '0009_habitacion_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicioHoteleria',
            fields=[
                ('idServicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=400)),
                ('horarioApertura', models.TimeField()),
                ('horarioCierre', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Subservicio',
            fields=[
                ('idSubservicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=400)),
                ('horarioApertura', models.TimeField()),
                ('horarioCierre', models.TimeField()),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VeranumApp.serviciohoteleria')),
            ],
        ),
    ]
