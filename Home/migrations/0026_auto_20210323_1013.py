# Generated by Django 3.1.4 on 2021-03-23 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0025_auto_20210323_0304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitios',
            old_name='Nombre',
            new_name='nombre',
        ),
    ]