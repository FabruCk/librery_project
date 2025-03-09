from django.db import models

#Creacion del los modelos para creacion de tablas

#Creacion del modelo autor
class Autor(models.Model):
    #Declaracion de los atributos de la tabla o clase
    id_autor = models.AutoField(primary_key=True, editable=False,db_column='T001IdAutor')#Declaracion de la PK de autor
    nombre = models.CharField(max_length=100, db_column='T001Nombre')#Declaracion del nombre
    apellido = models.CharField(max_length=100, db_column='T001Apellido')#Declaracion del apellido
    biografia = models.TextField(db_column='T001Biografia')#Declaracion de la biografia

    def __str__(self):
        return f"{self.nombre} {self.apellido}" #Retorno de los datos

    #Creacion de la tabla en base de datos
    class Meta:
        db_table = 'T001Autor'#Nombre de tabla
        #Asignacion de nomenclatura
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


#Creacion del modelo Editorial
class Editorial(models.Model):
    #Declaracion de los atributos de la tabla o clase
    id_editorial = models.AutoField(primary_key=True, editable=False,db_column='T002IdEditorial')#Declaracion de la PK de editorial
    nombre = models.CharField(max_length=100, db_column='T002Nombre')#Declaracion del nombre
    direccion = models.CharField(unique=True, max_length=100, db_column='T002Direccion')#Declaracion del direccion
    telefono = models.CharField(unique=True, max_length=100, db_column='T002Telefono')#Declaracion de la biografia

    def __str__(self):
        return f"{self.nombre}"

    #Creacion de la tabla en base de datos
    class Meta:
        db_table = 'T002Editorial'#Nombre de tabla
        #Asignacion de nomenclatura
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True, editable=False,db_column='T003IdLibro')
    titulo = models.CharField(max_length=100, db_column='T003Titulo')
    resumen = models.TextField(db_column='T003Resumen')
    isbn = models.CharField(max_length=100, db_column='T003ISBN')
    publicacion = models.DateField(db_column='T003AñoPublicacion')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE,related_name='libros', db_column='T003IdAutor')
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE,related_name='editorial', db_column='T003IdEditorial')

    def __str__(self):
        return f"{self.titulo}"

    class Meta:
        db_table = 'T003Libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'


class Miembro(models.Model):
    #Declaracion de los atributos de la tabla o clase
    id_miembro = models.AutoField(primary_key=True, editable=False,db_column='T004IdMiembro')#Declaracion de la PK de Miembro
    nombre = models.CharField(max_length=100, db_column='T004Nombre')#Declaracion del nombre
    apellido = models.CharField(max_length=100, db_column='T004Apellido')#Declaracion del apellido
    email = models.CharField(max_length=100, unique= True, db_column='T004Biografia')#Declaracion del email
    fecha_membresia = models.DateField(db_column='T004Membresia')#Fecha membresia

    def _str_(self):
        return f"{self.nombre} {self.apellido}" #Retorno de los datos

    #Creacion de la tabla en base de datos
    class Meta:
        db_table = 'T004Miembro'#Nombre de tabla
        #Asignacion de nomenclatura
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'


class Prestamo(models.Model):
    #Atributos de la clase
    id_prestamo = models.AutoField(primary_key=True, editable=False, db_column='T005Prestamo')
    fecha_inicial = models.DateField(db_column='T005FechaPrestamo')
    fecha_final = models.DateField(db_column='T005FechaDEvolucion')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamo', db_column='T005Libro')
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, related_name='miembro', db_column='T005Miembro')

    def __str__(self):
        return f"Prestamo de {self.libro.titulo} a {self.miembro.nombre}"
    
    class Meta:
        db_table = 'T005Prestamo'
        verbose_name = 'Prestamo'
        verbose_name_plural ='Prestamos'