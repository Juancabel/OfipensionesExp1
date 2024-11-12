from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import CronogramaForm
from .logic.cronograma_logic import get_cronogramas, create_cronograma
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import CronogramaSerializer
import json
from django.contrib.auth.decorators import login_required
from ofipensiones.auth0backend import getRole

@login_required
def cronograma_list(request):
    role = getRole(request)
    if role != "Administrador":
        return HttpResponse("Unauthorized User")
    cronogramas = get_cronogramas()
    serializer = CronogramaSerializer(cronogramas,many=True)
    context = {
        'cronograma_list': serializer.data
    }
    return render(request, 'cronograma/cronogramas.html', context)

def crear_cronograma(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = CronogramaForm(data)
        if form.is_valid():
            create_cronograma(form)
            messages.add_message(request, messages.SUCCESS, 'Cronograma creado exitosamente')
            return HttpResponseRedirect(reverse('cronogramaCreate'))
        else:
            print(form.errors)
    else:
        form = CronogramaForm()
    context = {
        'form': form,
    }
    return render(request, 'cronograma/cronogramaCreate.html', context)

    