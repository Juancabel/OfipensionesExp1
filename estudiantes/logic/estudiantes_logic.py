from ..models import Estudiante

def get_estudiantes():
    queryset = Estudiante.objects.all()
    return (queryset)

def get_estudiantes_aldia():
    queryset = Estudiante.objects.filter(cronograma__monto_total=0)
    return (queryset)

def create_estudiante(form):
    estudiante = form.save()
    estudiante.save()
    return ()

def get_estudiantes_padre(lista_ids):
    queryset = Estudiante.objects.filter(id__in=lista_ids) 
    return queryset