# -*- coding: utf-8 -*-
from django import forms
from django.forms import SelectDateWidget
__author__ = 'Rafael Boza Querol'
from universidad.models import *


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ["nombre_apellidos", "carnet"]

    nombre_apellidos = forms.CharField(
        required=True,
        label='Nombre y Apellidos del profesor',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
            }))

    carnet = forms.CharField(
        required=True,
        label='Carnet de identidad',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
            }))


class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ["nombre"]

    nombre = forms.CharField(
        required=True,
        label='Nombre de la ciudad',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
            }))


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ["nombre", "profesor_guia"]

    nombre = forms.CharField(
        required=True,
        label='Nombre del grupo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
            }))

    profesor_guia = forms.ModelChoiceField(
        queryset=Profesor.objects.all().order_by("nombre_apellidos"),
        required=True,
        label='Profesor guia',
        widget=forms.Select(
            attrs={'class': 'form-control'
                   }))


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["nombre_apellidos", "carnet",  "email", "fecha_nacimiento", "ciudad_nacimiento", "grupo"]

    nombre_apellidos = forms.CharField(
        required=True,
        label='Nombre y Apellidos del estudiante',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
            }))

    carnet = forms.CharField(
        required=True,
        label='Carnet de identidad',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
            }))

    email = forms.EmailField(
        required=True,
        label='Email del estudiante',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
            }))

    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento",
        required=True,
        widget=SelectDateWidget(years=range(1950, 2022))
        )

    ciudad_nacimiento = forms.ModelChoiceField(
        queryset=Ciudad.objects.all(),
        required=True,
        label='Ciudad de Nacimiento',
        widget=forms.Select(
            attrs={'class': 'form-control',
                   }))

    grupo = forms.ModelChoiceField(
        queryset=Grupo.objects.all(),
        required=True,
        label='Grupo del estudiante',
        widget=forms.Select(
            attrs={'class': 'form-control',
                   }))



