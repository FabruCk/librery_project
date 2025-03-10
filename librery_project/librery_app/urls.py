# Importa la función path del módulo de URLs de Django
from django.urls import path
# Importa las vistas desde el módulo views de la aplicación actual
from .views import (
    AutorList, CrearAutor,
    EditorialList, CrearEditorial,
    LibroList, CrearLibro, LibroByAutor, LibroByEditorial,
    MiembroList, CrearMiembro,
    PrestamoList, CrearPrestamo, PrestamoByFecha, PrestamoByMiembro
)

urlpatterns = [

    #AUTORES-----------AUTORES-----------AUTORES

    #Listar autores
    path('autores/', AutorList.as_view(), name='autor-list'),
    # Crear una nuevo autor
    path('autores/crear/', CrearAutor.as_view(), name='autor-crear'),
    

    #eDITORIAL----------------EDITORIAL---------------EDITORIAL

    #Listar editoriales
    path('editoriales/', EditorialList.as_view(), name='editorial-list'),
    #Crear nuevo editorial
    path('editoriales/crear/', CrearEditorial.as_view(), name='editorial-crear'),


    #LIBROS----------------LIBROS----------------LIBROS

    #Listar libros
    path('libros/', LibroList.as_view(), name='libro-list'),
    #Crear libro
    path('libros/crear/', CrearLibro.as_view(), name='libro-crear'),
    #Buscar libros por autor
    path('libros/autor/<int:idAutor>/', LibroByAutor.as_view(), name='libros_by_autor'),
    #Buscar libros por editorial
    path('libros/editorial/<int:idEditorial>/', LibroByEditorial.as_view(), name='libros_by_autor'),


    # MIEMBROS------------------MIEBROS------------MIEMBROS

    #Listar miembros
    path('miembros/', MiembroList.as_view(), name='miembro-list'),
    #Crear miembros
    path('miembros/crear/', CrearMiembro.as_view(), name='miembro-crear'),


    # PRESTAMOS------------------PRESTAMOS------------PRESTAMOS

    #Listar prestamos
    path('prestamos/', PrestamoList.as_view(), name='prestamo-list'),
    # Crear un prestamo
    path('prestamos/crear/', CrearPrestamo.as_view(), name='prestamo-crear'),
    # Buscar préstamos por fecha de préstamo
    path('prestamos/fecha/<str:fecha>/', PrestamoByFecha.as_view(), name='prestamos_by_fecha'),
    # Buscar préstamos por miembro
    path('prestamos/miembro/<int:idMiembro>/', PrestamoByMiembro.as_view(), name='prestamos_by_miembro'),
]