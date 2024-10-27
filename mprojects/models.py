from django.db import models

# Create your models here.


class Proyectos(models.Model):
    nombreProyecto = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombreProyecto

class Equipo(models.Model):
    nombreEquipo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombreEquipo

class Usuarios(models.Model):
    nombreUsuario = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombreUsuario

class Tareas(models.Model):
    tituloTarea = models.CharField(max_length=200)
    descripcion = models.TextField()
    fechaInicio = models.DateField()
    tiempoDuracionInicio = models.TimeField()
    fechaFin = models.DateField()
    tiempoDuracionFin = models.TimeField()
    equipoTrabajo = models.ForeignKey(Equipo,related_name='tareas', on_delete=models.CASCADE)
    responsable = models.ForeignKey(Usuarios, related_name='responsable', on_delete=models.CASCADE)
    ejecutor = models.ForeignKey(Usuarios, related_name='ejecutor', on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tituloTarea + ' - ' + self.proyecto.nombreProyecto
