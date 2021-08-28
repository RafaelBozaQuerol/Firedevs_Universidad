# -*- coding: utf-8 -*-
from Firedevs_Universidad.settings import CAPACIDAD_MAXIMA
from universidad.models import Estudiante
__author__ = 'Rafael Boza Querol'
import datetime
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def crear_lista_pages(listado):
    izquierda = 1
    derecha = listado.paginator.num_pages
    pagina_actual = listado.number

    if pagina_actual > 3:
        izquierda = pagina_actual-2
    if derecha-pagina_actual > 3:
        derecha = pagina_actual+2
    final = list(range(izquierda, derecha+1))
    if izquierda != 1:
        final.insert(0, 1)
    if derecha != listado.paginator.num_pages:
        final.append(listado.paginator.num_pages)
    return final


def paginar(request, lista_objetos):
    paginator = Paginator(lista_objetos, 5)
    try:
        pagina = int(request.GET.get("pagina", "1"))
    except ValueError:
        pagina = 1
    try:
        lista_objetos = paginator.page(pagina)
    except(InvalidPage, EmptyPage):
        lista_objetos = paginator.page(paginator.num_pages)
    return lista_objetos


def obtener_sexo(ci):
    if int(ci[9]) % 2 == 0:
        return 'M'
    else:
        return 'F'


def obtener_edad(ci):
    ci = int(ci)
    fecha = ci / 100000
    anno = fecha / 10000
    mes = (fecha / 100) % 100
    dia = fecha % 100
    if anno < 10:
        anno = '0' + str(anno)
    anno_actual = datetime.datetime.now().year % 100
    anno = ('19' + str(anno), '20' + str(anno))[int(anno) <= anno_actual]
    edad = datetime.datetime.now().year - int(anno)
    if int(mes) > datetime.datetime.now().month:
        edad -= 1
    elif int(mes) == datetime.datetime.now().month and int(dia) > datetime.datetime.now().day:
        edad -= 1
    return edad


def validar_capacidad(grupo_id):
    cantidad = Estudiante.objects.filter(grupo_id=grupo_id).count()
    if CAPACIDAD_MAXIMA > cantidad:
        return True
    return False
