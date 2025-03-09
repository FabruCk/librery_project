# Importa la función path del módulo de URLs de Django
from django.urls import path
# Importa las vistas desde el módulo views de la aplicación actual
from .views import (
    AutorList, CrearAutor,
    TareaList, TareaByFecha, TareaByRangoFechas, TareaByPersona
)

# Define la lista de patrones de URL para la aplicación 'api_app'
urlpatterns = [
    # Rutas para la gestión de personas
    # Lista de personas
    path('autores/', AutorList.as_view(), name='autor-list'),
    # Crear una nueva persona
    path('autores/crear/', CrearAutor.as_view(), name='autor-crear'),

]