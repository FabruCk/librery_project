# Importaciones necesarias para la vista

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import NotFound, ValidationError
from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import AutorSerializer, EditorialSerializer, LibroSerializer, MiembroSerializer, PrestamoSerializer

#------AUTOR-----------AUTOR-----------AUTOR-------------AUTOR--------------AUTOR----------------

#Listar y crear
class AutorList(generics.ListAPIView):
    queryset = Autor.objects.all()         #Conjunto de consultas para obtener autores
    serializer_class = AutorSerializer     #Serializador a usar

    #GET para listar
    def get(self,request):
        autores = Autor.objects.all() # obtiene los autores
        serializer = AutorSerializer(autores, many = True) # Serializa los autores
        if not autores:
            raise NotFound('No se encontraron autores.') #Mensaje en caso de no existir autores
        return Response({'success':True, 'detail': 'Listado de autores', 'data': serializer.data}, status=status.HTTP_200_OK)#Devuelve una respuesta del proceso
    
class CrearAutor(generics.CreateAPIView):
    queryset = Autor.objects.all()         #Conjunto de consultas para obtener autores
    serializer_class = AutorSerializer     #Serializador a usar

    #POST para crear
    def post(self, request):
        serializer = AutorSerializer(data = request.data) # selrializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':True, 'detail': 'Autor creado correctamenre', 'data': serializer.data}, status=status.HTTP_201_CREATED)#Devuelve una respuesta del proceso

#------EDITORIAL-------EDITORIAL------------EDITORIAL------------EDITORIAL-----------EDITORIAL--------

#LISTAR
class EditorialList(generics.ListAPIView):
    queryset = Editorial.objects.all()         #Conjunto de consultas para obtener autores
    serializer_class = EditorialSerializer     #Serializador a usar

    #GET para listar
    def get(self,request):
        editoriales = Editorial.objects.all() # obtiene los autores
        serializer = EditorialSerializer(editoriales, many = True) # Serializa los autores
        if not editoriales:
            raise NotFound('No se encontraron editoriales.') #Mensaje en caso de no existir autores
        return Response({'success':True, 'detail': 'Listado de editoriales', 'data': serializer.data}, status=status.HTTP_200_OK)#Devuelve una respuesta del proceso

#CREAR-----------

class CrearEditorial(generics.CreateAPIView):
    queryset = Editorial.objects.all()         #Conjunto de consultas para obtener autores
    serializer_class = EditorialSerializer     #Serializador a usar
    #POST para crear
    def post(self, request):
        serializer = EditorialSerializer(data = request.data) # serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':True, 'detail': 'Editorial creado correctamenre', 'data': serializer.data}, status=status.HTTP_201_CREATED)#Devuelve una respuesta del proceso
    
    
#--------LIBRO---------LIBRO---------LIBRO---------------LIBRO--------------LIBRO----------------

#LISTAR
class LibroList(generics.ListAPIView):
    queryset = Libro.objects.all()         #Conjunto de consultas para obtener autores
    serializer_class = LibroSerializer     #Serializador a usar

    #GET para listar
    def get(self,request):
        libros = Libro.objects.all() # obtiene los autores
        serializer = LibroSerializer(libros, many = True) # Serializa los autores
        if not libros:
            raise NotFound('No se encontraron libros.') #Mensaje en caso de no existir autores
        return Response({'success':True, 'detail': 'Listado de libros', 'data': serializer.data}, status=status.HTTP_200_OK)#Devuelve una respuesta del proceso
    
#CREAR-----------

class CrearLibro(generics.CreateAPIView):
    queryset = Libro.objects.all()         #Conjunto de consultas para obtener autores
    serializer_class = LibroSerializer     #Serializador a usar
    #POST para crear
    def post(self, request):
        serializer = LibroSerializer(data = request.data) # serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':True, 'detail': 'Libro creado correctamenre', 'data': serializer.data}, status=status.HTTP_201_CREATED)#Devuelve una respuesta del proceso
    
#------MIEMBRO--------MIEMBRO---------MIEMBRO----------MIEMBRO-----------MIEMBRO-------------------MIEMBRO-------------MIEMBRO----- 

#LISTAR
class MiembroList(generics.ListAPIView):
    queryset = Miembro.objects.all()         #Conjunto de consultas para obtener autores
    serializer_class = MiembroSerializer     #Serializador a usar

    #GET para listar
    def get(self,request):
        miembros = Miembro.objects.all() # obtiene los autores
        serializer = MiembroSerializer(miembros, many = True) # Serializa los autores
        if not miembros:
            raise NotFound('No se encontraron miembros.') #Mensaje en caso de no existir autores
        return Response({'success':True, 'detail': 'Listado de miembros', 'data': serializer.data}, status=status.HTTP_200_OK)#Devuelve una respuesta del proceso
    
#CREAR-----------

class CrearMiembro(generics.CreateAPIView):
    queryset = Miembro.objects.all()         #Conjunto de consultas para obtener autores
    serializer_class = MiembroSerializer     #Serializador a usar
    #POST para crear
    def post(self, request):
        serializer = MiembroSerializer(data = request.data) # serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':True, 'detail': 'Miembro creado correctamenre', 'data': serializer.data}, status=status.HTTP_201_CREATED)#Devuelve una respuesta del proceso

#---PRESTAMO-------PRESTAMO---------PRESTAMO-----------PRESTAMO-------PRESTAMO-----------PRESTAMO----
    
    #LISTAR
class PrestamoList(generics.ListAPIView):
    queryset = Prestamo.objects.all()         #Conjunto de consultas para obtener autores
    serializer_class = PrestamoSerializer     #Serializador a usar

    #GET para listar
    def get(self,request):
        prestamos = Prestamo.objects.all() # obtiene los autores
        serializer = PrestamoSerializer(prestamos, many = True) # Serializa los autores
        if not prestamos:
            raise NotFound('No se encontraron prestamos.') #Mensaje en caso de no existir autores
        return Response({'success':True, 'detail': 'Listado de prestamos', 'data': serializer.data}, status=status.HTTP_200_OK)#Devuelve una respuesta del proceso
    
#CREAR-----------

class CrearPrestamo(generics.CreateAPIView):
    queryset = Prestamo.objects.all()         #Conjunto de consultas para obtener autores
    serializer_class = PrestamoSerializer     #Serializador a usar
    #POST para crear
    def post(self, request):
        serializer = PrestamoSerializer(data = request.data) # serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success':True, 'detail': 'prestamo creado correctamenre', 'data': serializer.data}, status=status.HTTP_201_CREATED)#Devuelve una respuesta del proceso