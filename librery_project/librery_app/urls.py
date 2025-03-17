# Importa la función path del módulo de URLs de Django
from django.urls import path
# Importa las vistas desde el módulo views de la aplicación actual
from .views import (
    list_project,
    create_autor, listar_autores, delete_autor,
    create_editorial, listar_editoriales, delete_editorial
)

urlpatterns = [
    #Mostrar
    path('', list_project),
    path('crearautor/', create_autor, name='crear-autor'),
    path('listar_autores/', listar_autores, name='listar-autores'),
    path('borrar_autor/<int:id_autor>/', delete_autor, name='borrar-autor'),
    path('creareditorial/', create_editorial, name='crear-editorial'),
    path('listar_editoriales/', listar_editoriales, name='listar-editoriales'),
    path('borrar_editorial/<int:id_editorial>/', delete_editorial, name='borrar-editorial')
]