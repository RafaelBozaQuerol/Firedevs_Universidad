# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'Rafael Boza Querol'
from django.contrib import messages
from django.shortcuts import render, redirect
from universidad.forms import ProfesorForm
from universidad.models import Profesor
from universidad.utiles import paginar, crear_lista_pages


def gestion_profesores(request):
    entities = Profesor.objects.all()
    entities = paginar(request, entities)
    paginas = crear_lista_pages(entities)
    nombre_pag = "Listado de Profesores"
    context = {'entities': entities, 'paginas': paginas, 'nombre_pag': nombre_pag, 'tittle_page': nombre_pag}
    return render(request, "Profesores/gestion_profesor.html", context)


def registrar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)

        if form.is_valid():
            profesor = form.save(commit=False)
            profesor.save()

            messages.add_message(request, messages.SUCCESS, "Registrado con éxito.")
            return redirect('/profesores')
        else:
            context = {'form': form, 'nombre_form': "Registrar:", 'tittle_page': 'Registrar {0}'.format(form.Meta.model.__name__)}
            return render(request, "Profesores/registrar_profesor.html", context)
    else:
        form = ProfesorForm()
    context = {'form': form, 'nombre_form': "Registrar:", 'tittle_page': 'Registrar {0}'.format(form.Meta.model.__name__)}
    return render(request, "Profesores/registrar_profesor.html", context)


def modificar_profesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)

    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)

        if form.is_valid():
            profesor = form.save(commit=False)
            profesor.save()

            messages.add_message(request, messages.SUCCESS, "Modificado con éxito.")
            return redirect('/profesores')
        else:
            context = {'form': form, 'nombre_form': "Modificar:", 'tittle_page': 'Modificar {0}'.format(form.Meta.model.__name__)}
            return render(request, "Profesores/modificar_profesor.html", context)
    else:
        form = ProfesorForm(instance=profesor)

    context = {'form': form, 'nombre_form': "Modificar:", 'tittle_page': 'Modificar {0}'.format(form.Meta.model.__name__)}
    return render(request, "Profesores/modificar_profesor.html", context)


def eliminar_profesor(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()
    messages.add_message(request, messages.SUCCESS, "Eliminado con éxito.")
    return redirect('/profesores')