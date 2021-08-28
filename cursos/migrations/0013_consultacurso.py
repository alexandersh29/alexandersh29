# Generated by Django 3.2.4 on 2021-08-06 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0012_delete_consultacurso'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaCurso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('titulo_curso', models.TextField(verbose_name='Titulo del Curso')),
                ('descripcion', models.TextField(verbose_name='Descripción del curso')),
                ('duracion', models.CharField(max_length=20, verbose_name='Duración del curso')),
                ('categoria', models.CharField(max_length=15, verbose_name='Categoría del curso')),
                ('costo', models.FloatField(verbose_name='Costo del curso')),
                ('estado', models.BooleanField(verbose_name='Curso activo')),
                ('imagen', models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
            ],
            options={
                'verbose_name': 'Consulta Curso',
                'verbose_name_plural': 'Consultas Cursos',
                'ordering': ['-created'],
            },
        ),
    ]
