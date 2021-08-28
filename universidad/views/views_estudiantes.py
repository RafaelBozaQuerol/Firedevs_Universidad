# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'Rafael Boza Querol'
from django.contrib import messages
from django.shortcuts import render, redirect
from universidad.forms import EstudianteForm
from universidad.models import Estudiante
from universidad.utiles import paginar, crear_lista_pages, obtener_edad, obtener_sexo, validar_capacidad


def gestion_estudiantes(request):
    entities = Estudiante.objects.all()
    entities = paginar(request, entities)
    paginas = crear_lista_pages(entities)
    nombre_pag = "Listado de Estudiantes"
    context = {'entities': entities, 'paginas': paginas, 'nombre_pag': nombre_pag, 'tittle_page': nombre_pag}
    return render(request, "Estudiantes/gestion_estudiante.html", context)


def registrar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False)
            if validar_capacidad(estudiante.grupo_id):
                estudiante.edad = obtener_edad(estudiante.carnet)
                estudiante.sexo = obtener_sexo(estudiante.carnet)
                estudiante.save()
                messages.add_message(request, messages.SUCCESS, "Registrado con éxito.")
                return redirect('/estudiantes')
            else:
                messages.add_message(request, messages.WARNING, "El grupo seleccionado está a máxima capacidad.")
                context = {'form': form, 'nombre_form': "Registrar:", 'tittle_page': 'Registrar {0}'.format(form.Meta.model.__name__)}
                return render(request, "Estudiantes/registrar_estudiante.html", context)

        else:
            context = {'form': form, 'nombre_form': "Registrar:", 'tittle_page': 'Registrar {0}'.format(form.Meta.model.__name__)}
            return render(request, "Estudiantes/registrar_estudiante.html", context)
    else:
        form = EstudianteForm()
    context = {'form': form, 'nombre_form': "Registrar:", 'tittle_page': 'Registrar {0}'.format(form.Meta.model.__name__)}
    return render(request, "Estudiantes/registrar_estudiante.html", context)


def modificar_estudiante(request, id_estudiante):
    estudiante = Estudiante.objects.get(id=id_estudiante)

    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)

        if form.is_valid():
            estudiante = form.save(commit=False)
            estudiante.edad = obtener_edad(estudiante.carnet)
            estudiante.sexo = obtener_sexo(estudiante.carnet)
            estudiante.save()

            messages.add_message(request, messages.SUCCESS, "Modificado con éxito.")
            return redirect('/estudiantes')
        else:
            context = {'form': form, 'nombre_form': "Modificar:", 'tittle_page': 'Modificar {0}'.format(form.Meta.model.__name__)}
            return render(request, "Estudiantes/modificar_estudiante.html", context)
    else:
        form = EstudianteForm(instance=estudiante)

    context = {'form': form, 'nombre_form': "Modificar:", 'tittle_page': 'Modificar {0}'.format(form.Meta.model.__name__)}
    return render(request, "Estudiantes/modificar_estudiante.html", context)


def eliminar_estudiante(request, id_estudiante):
    estudiante = Estudiante.objects.get(id=id_estudiante)
    estudiante.delete()
    messages.add_message(request, messages.SUCCESS, "Eliminado con éxito.")
    return redirect('/estudiantes')