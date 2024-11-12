from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('estudiantes/', views.estudiante_list),
    path('estudiantes/aldia/', views.estudiante_list_al_dia),
    path('estudiantes/padre/', views.estudiante_padre),
    path('estudiantescreate/', csrf_exempt(views.crear_estudiante), name='estudianteCreate'),
]