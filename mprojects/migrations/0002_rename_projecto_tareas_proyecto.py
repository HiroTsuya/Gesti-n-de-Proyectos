# Generated by Django 5.1.2 on 2024-10-21 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mprojects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tareas',
            old_name='projecto',
            new_name='proyecto',
        ),
    ]
