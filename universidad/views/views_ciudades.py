# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'Rafael Boza Querol'
from django.contrib import messages
from django.shortcuts import render, redirect

from universidad.forms import CiudadForm
from universidad.models import Ciudad
from universidad.utiles import paginar, crear_lista_pages


def gestion_ciudades(request):
    entities = Ciudad.objects.all()
    entities = paginar(request, entities)
    paginas = crear_lista_pages(entities)
    nombre_pag = "Listado de Ciudades"
    context = {'entities': entities, 'paginas': paginas, 'nombre_pag': nombre_pag, 'tittle_page': nombre_pag}
    return render(request, "Ciudades/gestion_ciudad.html", context)


def registrar_ciudad(request):

    if request.method == 'POST':
        form = CiudadForm(request.POST)

        if form.is_valid():
            ciudad = form.save(commit=False)
            ciudad.save()

            messages.add_message(request, messages.SUCCESS, "Registrado con éxito.")
            return redirect('/ciudades')
        else:
            context = {'form': form, 'nombre_form': "Registrar:", 'tittle_page': 'Registrar {0}'.format(form.Meta.model.__name__)}
            return render(request, "Ciudades/registrar_ciudad.html", context)
    else:
        form = CiudadForm()
    context = {'form': form, 'nombre_form': "Registrar:", 'tittle_page': 'Registrar {0}'.format(form.Meta.model.__name__)}
    return render(request, "Ciudades/registrar_ciudad.html", context)


def modificar_ciudad(request, id_ciudad):
    ciudad = Ciudad.objects.get(id=id_ciudad)

    if request.method == 'POST':
        form = CiudadForm(request.POST, instance=ciudad)

        if form.is_valid():
            ciudad = form.save(commit=False)
            ciudad.save()

            messages.add_message(request, messages.SUCCESS, "Modificado con éxito.")
            return redirect('/ciudades')
        else:
            context = {'form': form, 'nombre_form': 'Modificar:', 'tittle_page': 'Modificar {0}'.format(form.Meta.model.__name__)}
            return render(request, "Ciudades/modificar_ciudad.html", context)
    else:
        form = CiudadForm(instance=ciudad)

    context = {'form': form, 'nombre_form': 'Modificar:', 'tittle_page': 'Modificar {0}'.format(form.Meta.model.__name__)}
    return render(request, "Ciudades/modificar_ciudad.html", context)


def eliminar_ciudad(request, id_ciudad):
    ciudad = Ciudad.objects.get(id=id_ciudad)
    ciudad.delete()
    messages.add_message(request, messages.SUCCESS, "Eliminado con éxito.")
    return redirect('/ciudades')