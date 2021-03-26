# Generated by Django 3.1.4 on 2021-02-27 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_auto_20210226_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aplicaciones',
            name='subtitulo',
        ),
        migrations.RemoveField(
            model_name='caracteriticas',
            name='subtitulo',
        ),
        migrations.AddField(
            model_name='aplicacion',
            name='subtitulo',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='subtitulo',
            field=models.CharField(default=5, max_length=60),
            preserve_default=False,
        ),
    ]
