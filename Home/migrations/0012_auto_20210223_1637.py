# Generated by Django 3.1.4 on 2021-02-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_auto_20210223_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planes',
            name='dispositivos',
            field=models.CharField(choices=[('1/4', '1/4'), ('5/8', '5/8'), ('9/15', '9/15'), ('10/25', '10/25')], max_length=20),
        ),
    ]
