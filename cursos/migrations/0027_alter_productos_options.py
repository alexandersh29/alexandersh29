# Generated by Django 3.2.4 on 2021-08-25 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0026_auto_20210824_2337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productos',
            options={'ordering': ['created'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]
