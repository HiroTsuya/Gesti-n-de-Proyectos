# Generated by Django 5.1.2 on 2024-10-21 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mprojects', '0002_rename_projecto_tareas_proyecto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tareas',
            old_name='fechafin',
            new_name='fechaFin',
        ),
        migrations.RenameField(
            model_name='tareas',
            old_name='fechainicio',
            new_name='fechaInicio',
        ),
    ]
