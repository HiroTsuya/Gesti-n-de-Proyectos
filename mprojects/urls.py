from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('proyectos/eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('tareas/', views.tareas, name='tareas'),
    path('tareas/eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('crear_proyecto/', views.crear_proyecto, name='crear_proyecto'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_equipo/', views.crear_equipo, name='crear_equipo'),
    path('equipos/', views.equipos, name='equipos'),
    path('equipos/eliminar/<int:equipo_id>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
]
