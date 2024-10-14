from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import FacturaForm
from .logic.facturas_logic import get_facturas, create_factura
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import FacturaSerializer
import json

def facturas_list(request):
    facturas = get_facturas()
    serializer = FacturaSerializer(facturas,many=True)
    context = {
        'factura_list': serializer.data
    }
    return JsonResponse(context)

def crear_factura(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = FacturaForm(data)
        if form.is_valid():
            create_factura(form)
            return JsonResponse({"mensaje": "Factura creada exitosamente"}, status=201)
        else:
            print(form.errors)
            return JsonResponse({"mensaje": "No se pudo crear la factura"}, status=500)
    else:
        return JsonResponse({"mensaje": "No se pudo crear la factura"}, status=500)
    
    