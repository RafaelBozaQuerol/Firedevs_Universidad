# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'Rafael Boza Querol'
from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    context = {
        'title': 'Home Page',
        'year': datetime.now().year
        , 'tittle_page': 'Inicio'
    }
    return render(request, 'universidad/index.html', context)






