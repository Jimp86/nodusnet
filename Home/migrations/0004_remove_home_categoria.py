# Generated by Django 3.0.9 on 2021-02-18 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20210218_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='categoria',
        ),
    ]