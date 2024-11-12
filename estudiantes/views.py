from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import EstudianteForm
from .logic.estudiantes_logic import get_estudiantes,get_estudiantes_aldia,create_estudiante,get_estudiantes_padre
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import EstudianteSerializer
import json
from django.contrib.auth.decorators import login_required
from ofipensiones.auth0backend import getRole,getKids

@login_required
def estudiante_list(request):
    role = getRole(request)
    if role != "Administrador":
        return HttpResponse("Unauthorized User")
    estudiantes = get_estudiantes()
    serializer = EstudianteSerializer(estudiantes,many=True)
    context = {
        'estudiante_list': serializer.data
    }
    return render(request, 'estudiantes/estudiantes.html', context)

@login_required
def estudiante_list_al_dia(request):
    role = getRole(request)
    if role != "Administrador":
        return HttpResponse("Unauthorized User")
    estudiantes = get_estudiantes_aldia()
    serializer = EstudianteSerializer(estudiantes,many=True)
    context = {
        'estudiante_list_al_dia': serializer.data
    }
    return render(request, 'estudiantes/estudiantes.html', context)

@login_required
def crear_estudiante(request):
    role = getRole(request)
    if role != "Administrador":
        return HttpResponse("Unauthorized User")
    if request.method == 'POST':
        data = json.loads(request.body)
        form = EstudianteForm(data)
        if form.is_valid():
            create_estudiante(form)
            messages.add_message(request, messages.SUCCESS, 'Estudiante creado exitosamente')
            return HttpResponseRedirect(reverse('estudianteCreate'))
        else:
            print(form.errors)
    else:
        form = EstudianteForm()
    context = {
        'form': form,
    }
    return render(request, 'estudiantes/estudianteCreate.html', context)

@login_required
def estudiante_padre(request):
    role = getRole(request)
    if role != "Padre":
        return HttpResponse("Unauthorized User")
    kids = getKids(request)
    estudiantes = get_estudiantes_padre(kids)
    serializer = EstudianteSerializer(estudiantes,many=True)
    context = {
        'estudiante_list_al_dia': serializer.data
    }
    return render(request, 'estudiantes/estudiantes.html', context)

    