# Generated by Django 4.2.1 on 2023-06-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VeranumApp', '0008_remove_habitacion_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='imagen',
            field=models.ImageField(default='static/img/habitacion-prueba.jpg', upload_to='static/img'),
        ),
    ]
