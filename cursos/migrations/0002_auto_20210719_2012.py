# Generated by Django 3.2.4 on 2021-07-20 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursos',
            options={'ordering': ['created'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AddField(
            model_name='cursos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='categoria',
            field=models.CharField(max_length=15, verbose_name='Categoría del curso'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='costo',
            field=models.FloatField(verbose_name='Costo del curso'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='descripcion',
            field=models.TextField(verbose_name='Descripción del curso'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='duracion',
            field=models.CharField(max_length=20, verbose_name='Duración del curso'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='estado',
            field=models.BooleanField(verbose_name='Curso activo'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='titulo_curso',
            field=models.TextField(verbose_name='Titulo del Curso'),
        ),
    ]
