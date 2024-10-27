from django import forms
from .models import Proyectos, Equipo, Usuarios

class crearNuevoProyecto(forms.Form):
    titulo = forms.CharField(label='Titutlo de Proyecto ', max_length=200)

class crearNuevoUsuario(forms.Form):
    nombre = forms.CharField(label='Nombre de nuevo usuario ', max_length=50)

class crearNuevoEquipo(forms.Form):
    nombre = forms.CharField(label='Nombre de nuevo equipo ', max_length=100)

class crearNuevaTarea(forms.Form):
    titulo = forms.CharField(label='Titutlo de Tarea ', max_length=200)
    descripcion = forms.CharField(label='Descripcion de Tarea ', widget=forms.Textarea)
    fechaInicio = forms.DateField(label='Fecha inicio de Tarea ', widget=forms.SelectDateWidget)
    tiempoDuracionInicio = forms.TimeField(label='Hora inicio de Tarea ', widget=forms.TimeInput)
    fechaFin = forms.DateField(label='Fecha fin de Tarea ', widget=forms.SelectDateWidget)
    tiempoDuracionFin = forms.TimeField(label='Hora fin de Tarea ', widget=forms.TimeInput)
    equipoTrabajo = forms.ModelChoiceField(queryset=Equipo.objects.all(), label='Equipo de trabajo ')
    responsable = forms.ModelChoiceField(queryset=Usuarios.objects.all(), label='Responsable ')
    ejecutor = forms.ModelChoiceField(queryset=Usuarios.objects.all(), label='Ejecutor ')
    proyecto = forms.ModelChoiceField(queryset=Proyectos.objects.all(), label='Proyecto ')