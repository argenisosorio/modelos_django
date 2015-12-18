#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from encuesta.views import *
import encuesta.views as views



urlpatterns = patterns('',
    url(r'^$','encuesta.views.index', name='index'),
    url(r'^registrar/', Registrar.as_view(), name='registrar'),
    url(r'^confirmacion_registro/', Confirmacion_registro.as_view(), name='confirmacion_registro'),
    url(r'^consultar/', Consultar.as_view(), name='consultar'),
)