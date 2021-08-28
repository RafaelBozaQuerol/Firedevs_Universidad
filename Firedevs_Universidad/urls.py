
from django.conf.urls import url
from django.contrib import admin

from universidad.views.views_ciudades import *
from universidad.views.views_estudiantes import *
from universidad.views.views_grupos import *
from universidad.views.views_initial import home
from universidad.views.views_profesores import *
from universidad.views.views_reportes import reporte_estudiantes_grupos

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^$', home),
        url(r'^reporte_estudiantes$', reporte_estudiantes_grupos, name='reporte_estudiantes'),


        url(r'^estudiantes/$', gestion_estudiantes, name='estudiantes'),
        url(r'^estudiantes/registrar_estudiante/$', registrar_estudiante, name='registrar_estudiante'),
        url(r'^estudiantes/(?P<id_estudiante>[\w]+)/eliminar/$', eliminar_estudiante, name='eliminar_estudiante'),
        url(r'^estudiantes/(?P<id_estudiante>[\w]+)/modificar/$', modificar_estudiante, name='modificar_estudiante'),

        url(r'^profesores/$', gestion_profesores, name='profesores'),
        url(r'^profesores/registrar_profesor/$', registrar_profesor, name='registrar_profesor'),
        url(r'^profesores/(?P<id_profesor>[\w]+)/eliminar/$', eliminar_profesor, name='eliminar_profesor'),
        url(r'^profesores/(?P<id_profesor>[\w]+)/modificar/$', modificar_profesor, name='modificar_profesor'),

        url(r'^ciudades/$', gestion_ciudades, name='ciudades'),
        url(r'^ciudades/registrar_ciudad/$', registrar_ciudad, name='registrar_ciudad'),
        url(r'^ciudades/(?P<id_ciudad>[\w]+)/eliminar/$', eliminar_ciudad, name='eliminar_ciudad'),
        url(r'^ciudades/(?P<id_ciudad>[\w]+)/modificar/$', modificar_ciudad, name='modificar_ciudad'),

        url(r'^grupos/$', gestion_grupos, name='grupos'),
        url(r'^grupos/registrar_grupo/$', registrar_grupo, name='registrar_grupo'),
        url(r'^grupos/(?P<id_grupo>[\w]+)/eliminar/$', eliminar_grupo, name='eliminar_grupo'),
        url(r'^grupos/(?P<id_grupo>[\w]+)/modificar/$', modificar_grupo, name='modificar_grupo'),
        url(r'^grupos/(?P<id_grupo>[\w]+)/detalles/$', detalles_grupo, name='detalles_grupo'),
]
