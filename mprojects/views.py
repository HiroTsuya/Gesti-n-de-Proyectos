from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyectos, Usuarios, Equipo, Tareas
from .forms import crearNuevaTarea, crearNuevoProyecto, crearNuevoEquipo, crearNuevoUsuario
from datetime import datetime
# Create your views here.


def index(request):
    return render(request, 'index.html')

def proyectos(request):
    proyectos = Proyectos.objects.all()
    return render(request, 'proyectos.html', {
        'proyectos': proyectos
    })

def tareas(request):
    tareas = Tareas.objects.all()
    return render(request, 'tareas.html', {
        'tareas': tareas
    })

def usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuarios.html', {
        'usuarios': usuarios
    })

def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos.html', {
        'equipos': equipos
    })

def crear_tarea(request):
    if request.method == 'GET':
        return render(request, 'crear_tarea.html', {
            'form':crearNuevaTarea()
            })
    else:
        fecha_inicio = datetime(
            int(request.POST['fechaInicio_year']),
            int(request.POST['fechaInicio_month']),
            int(request.POST['fechaInicio_day'])
        )
        fecha_fin = datetime(
            int(request.POST['fechaFin_year']),
            int(request.POST['fechaFin_month']),
            int(request.POST['fechaFin_day'])
        )
        Tareas.objects.create(
            tituloTarea=request.POST['titulo'],
            descripcion=request.POST['descripcion'],
            fechaInicio=fecha_inicio,
            tiempoDuracionInicio=request.POST['tiempoDuracionInicio'],
            fechaFin=fecha_fin,
            tiempoDuracionFin=request.POST['tiempoDuracionFin'],
            equipoTrabajo_id=request.POST['equipoTrabajo'],
            responsable_id=request.POST['responsable'],
            ejecutor_id=request.POST['ejecutor'],
            proyecto_id=request.POST['proyecto'])
        return redirect('tareas')

def crear_proyecto(request):
    if request.method == 'GET':
        return render(request, 'crear_proyecto.html', {
            'form':crearNuevoProyecto()
        })
    else:
        Proyectos.objects.create(nombreProyecto=request.POST['titulo'])
        return redirect('proyectos')

def crear_equipo(request):
    if request.method == 'GET':
        return render(request, 'crear_equipo.html', {
            'form':crearNuevoEquipo
        })
    else:
        Equipo.objects.create(nombreEquipo=request.POST['nombre'])
        return redirect('equipos')

def crear_usuario(request):
    if request.method == 'GET':
        return render(request, 'crear_usuario.html', {
            'form':crearNuevoUsuario
        })
    else:
        Usuarios.objects.create(nombreUsuario=request.POST['nombre'])
        return redirect('usuarios')

def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyectos, pk=proyecto_id)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('proyectos')

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tareas, pk=tarea_id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas')

def eliminar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('equipos')

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuarios, pk=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios')
