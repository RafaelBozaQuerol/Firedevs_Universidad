from __future__ import unicode_literals
__author__ = 'Rafael Boza Querol'
from django.core.validators import RegexValidator
# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.


class Profesor(models.Model):
    carnet = models.CharField(max_length=11, unique=True, validators=[RegexValidator(regex='^[0-9]{2}(0[1-9]|1[0-2])(31|30|(0[1-9]|[1-2][0-9]))[0-9]{5}$', message='CI incorrecto', )])
    nombre_apellidos = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre_apellidos

    class Meta:
        ordering = ["nombre_apellidos"]


class Grupo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    profesor_guia = models.ForeignKey(Profesor, on_delete=models.DO_NOTHING)
    capacidad = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]


class Estudiante(models.Model):
    SEXO = [('M', 'Masculino'), ('F', 'Femenino')]
    carnet = models.CharField(max_length=11, unique=True, validators=[RegexValidator(regex='^[0-9]{2}(0[1-9]|1[0-2])(31|30|(0[1-9]|[1-2][0-9]))[0-9]{5}$', message='CI incorrecto',)])
    nombre_apellidos = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)
    sexo = models.CharField(max_length=1, choices=SEXO)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    ciudad_nacimiento = models.ForeignKey(Ciudad, on_delete=models.DO_NOTHING)
    grupo = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.nombre_apellidos

    def get_sexo(self):
        return 'Masculino' if self.sexo == 'M' else 'Femenino'

    class Meta:
        ordering = ["nombre_apellidos"]
