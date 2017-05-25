# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class Patrocinador(models.Model):
    usuario = models.OneToOneField(User)
    """Acá tu agregas el resto de los campos y vuelves 
        a migrar, es decir, agregas los atributos y usas estos comandos:
         python manage.py makemigrations
         python manage.py migrate
    """


class Alumno(models.Model):
    usuario = models.OneToOneField(User)


class Administrador(models.Model):
    usuario = models.OneToOneField(User)