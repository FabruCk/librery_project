# Importa la función path del módulo de URLs de Django
from django.urls import path
# Importa las vistas desde el módulo views de la aplicación actual
from .views import (
    AutorList, CrearAutor,
    EditorialList, CrearEditorial,
    LibroList, CrearLibro, LibroByAutor, LibroByEditorial,
    MiembroList, CrearMiembro,
    PrestamoList, CrearPrestamo,
)

# Define la lista de patrones de URL para la aplicación 'api_app'
urlpatterns = [
    # Rutas para la gestión de personas
    # Lista de personas
    path('autores/', AutorList.as_view(), name='autor-list'),
    # Crear una nueva persona
    path('autores/crear/', CrearAutor.as_view(), name='autor-crear'),

    # Lista de personas
    path('editoriales/', EditorialList.as_view(), name='editorial-list'),
    # Crear una nueva persona
    path('editoriales/crear/', CrearEditorial.as_view(), name='editorial-crear'),

        # Lista de personas
    path('libros/', LibroList.as_view(), name='libro-list'),
    # Crear una nueva persona
    path('libros/crear/', CrearLibro.as_view(), name='libro-crear'),
    #Buscar libros por autor
    path('libros/autor/<int:idAutor>/', LibroByAutor.as_view(), name='libros_by_autor'),

    path('libros/editorial/<int:idEditorial>/', LibroByEditorial.as_view(), name='libros_by_autor'),


        # Lista de personas
    path('miembro/', MiembroList.as_view(), name='miembro-list'),
    # Crear una nueva persona
    path('miembro/crear/', CrearMiembro.as_view(), name='miembro-crear'),

        # Lista de personas
    path('prestamos/', PrestamoList.as_view(), name='prestamo-list'),
    # Crear una nueva persona
    path('prestamos/crear/', CrearPrestamo.as_view(), name='prestamo-crear'),
]