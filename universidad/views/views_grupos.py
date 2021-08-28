# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'Rafael Boza Querol'
from django.contrib import messages
from django.shortcuts import render, redirect

from universidad.forms import GrupoForm
from universidad.models import Grupo, Estudiante
from universidad.utiles import paginar, crear_lista_pages


def gestion_grupos(request):
    entities = Grupo.objects.all()
    entities = paginar(request, entities)
    paginas = crear_lista_pages(entities)
    nombre_pag = "Listado de Grupos"
    context = {'entities': entities, 'paginas': paginas, 'nombre_pag': nombre_pag, 'tittle_page': nombre_pag}
    return render(request, "Grupos/gestion_grupo.html", context)


def registrar_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)

        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.save()

            messages.add_message(request, messages.SUCCESS, "Registrado con éxito.")
            return redirect('/grupos')
        else:
            context = {'form': form, 'nombre_form': "Registrar:", 'tittle_page': 'Registrar {0}'.format(form.Meta.model.__name__)}
            return render(request, "Grupos/registrar_grupo.html", context)
    else:
        form = GrupoForm()
    context = {'form': form, 'nombre_form': "Registrar:", 'tittle_page': 'Registrar {0}'.format(form.Meta.model.__name__)}
    return render(request, "Grupos/registrar_grupo.html", context)


def modificar_grupo(request, id_grupo):
    grupo = Grupo.objects.get(id=id_grupo)
    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.save()
            messages.add_message(request, messages.SUCCESS, "Modificado con éxito.")
            return redirect('/grupos')
        else:
            context = {'form': form, 'nombre_form': "Modificar:", 'tittle_page': 'Modificar {0}'.format(form.Meta.model.__name__)}
            return render(request, "Grupos/modificar_grupo.html", context)
    else:
        form = GrupoForm(instance=grupo)

    context = {'form': form, 'nombre_form': "Modificar:", 'tittle_page': 'Modificar {0}'.format(form.Meta.model.__name__)}
    return render(request, "Grupos/modificar_grupo.html", context)


def eliminar_grupo(request, id_grupo):
    grupo = Grupo.objects.get(id=id_grupo)
    grupo.delete()
    messages.add_message(request, messages.SUCCESS, "Eliminado con éxito.")
    return redirect('/grupos')


def detalles_grupo(request, id_grupo):
    entities = Estudiante.objects.filter(grupo__id=id_grupo)
    grupo = Grupo.objects.get(id=id_grupo)
    entities = paginar(request, entities)
    paginas = crear_lista_pages(entities)
    nombre_pag = 'Estudiantes del grupo [{0}]'.format(grupo)
    context = {'entities': entities, 'paginas': paginas, 'nombre_pag': nombre_pag, 'tittle_page': nombre_pag}
    return render(request, "Grupos/estudiantes_grupo.html", context)
