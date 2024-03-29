# Generated by Django 5.0.2 on 2024-02-16 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciclo', models.PositiveIntegerField()),
                ('paralelo', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APPasistencias.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APPasistencias.materia')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAsistencia', models.DateField()),
                ('asistio', models.BooleanField()),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APPasistencias.estudiante')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APPasistencias.materia')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencia_list', to='APPasistencias.profesor')),
            ],
        ),
    ]
