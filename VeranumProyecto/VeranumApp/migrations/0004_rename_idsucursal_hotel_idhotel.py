# Generated by Django 4.2.1 on 2023-06-13 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VeranumApp', '0003_alter_hotel_idsucursal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='idSucursal',
            new_name='idHotel',
        ),
    ]