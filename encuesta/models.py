#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from encuesta.constantes import *


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=8)
    telefono = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)    
    nacionalidad = models.CharField(max_length=1, choices=NACIONALIDAD)
    fecha = models.DateField(default=datetime.now, help_text='Fecha en que realizó la encuesta')
    pregunta1 = models.TextField(max_length=200)
    terminos = models.BooleanField(default=False)


    def __unicode__(self):
        return self.nombre