# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from models import *
from django.core.exceptions import ObjectDoesNotExist


class IndexView(TemplateView):
    template_name = "index.html"


def login_alumno(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/alumno/')
            else:
                return render_to_response('login_error.html', {})
        else:
            return HttpResponseRedirect('/login_alumno/')
    else:
        return render(request, 'login_alumno.html', {})


def login_patrocinador(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/patrocinador/')
            else:
                return render_to_response('login_error.html', {})
        else:
            return HttpResponseRedirect('/login_patrocinador/')
    else:
        return render(request, 'login_patrocinador.html', {})


def login_administrador(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/administrador/')
            else:
                return render_to_response('login_error.html', {})
        else:
            return HttpResponseRedirect('/login_administrador/')
    else:
        return render(request, 'login_administrador.html', {})


@login_required
def indexalumno(request):
    current = request.user
    try:
        profile = Alumno.objects.get(usuario=current)
        if profile:
            return render_to_response('index_alumno.html', {})
        else:
            return render_to_response('login_error.html', {})
    except ObjectDoesNotExist:
        return render_to_response('login_error.html', {})


@login_required
def indexpatrocinador(request):
    current = request.user
    try:
        profile = Patrocinador.objects.get(usuario=current)
        if profile:
            return render_to_response('index_patrocinador.html', {})
        else:
            return render_to_response('login_error.html', {})
    except ObjectDoesNotExist:
        return render_to_response('login_error.html', {})


@login_required
def indexadministrador(request):
    current = request.user
    try:
        profile = Administrador.objects.get(usuario=current)
        if profile:
            return render_to_response('index_administrador.html', {})
        else:
            return render_to_response('login_error.html', {})
    except ObjectDoesNotExist:
        return render_to_response('login_error.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')