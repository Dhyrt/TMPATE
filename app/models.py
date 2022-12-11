from django.db import models

# Create your models here.
class TipoPefil(models.Model):
    id_perfil = models.IntegerField(primary_key=True)
    nombre_perfil = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre_perfil
    
    class Meta:
        db_table = 'db_tipoUsuario'

class Genero(models.Model):
    id_genero = models.IntegerField(primary_key=True)
    genero = models.CharField(max_length=20)

    def __str__(self):
        return self.genero

    class Meta:
        db_table = 'db_genero'

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=20)
    p_nombre = models.CharField(max_length=20)
    s_nombre = models.CharField(max_length=20)
    p_apellido = models.CharField(max_length=20)
    s_apellido = models.CharField(max_length=20)
    nombre_usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=20)
    TipoUsuario = models.ForeignKey(TipoPefil, on_delete=models.CASCADE)
    Genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut

    class Meta:
        db_table = 'db_usuario'

class Credencial(models.Model):
    id_credencial = models.IntegerField(primary_key=True)
    habilitado = models.CharField(max_length=1)
    fecha = models.DateField()

    def __str__(self):
        return str(self.id_credencial)
    
    class Meta:
        db_table = 'db_credencial'

class Autentificacion(models.Model):
    id_autentificacion = models.IntegerField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=20)
    rut_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_credencial = models.ForeignKey(Credencial, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_usuario

    class Meta:
        db_table = 'db_autentificacion'

class Discapacidad(models.Model):
    id_discapacidad = models.IntegerField(primary_key=True)
    discapacidad = models.CharField(max_length=20)

    def __str__(self):
        return self.discapacidad

    class Meta:
        db_table = 'db_discapacidad'

class AdultoMayor(models.Model):
    id_adultoMayor = models.IntegerField(primary_key=True)
    discapacidad = models.BooleanField()
    rut_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_discapacidad = models.ForeignKey(Discapacidad, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_adultoMayor)

    class Meta:
        db_table = 'db_adultoMayor'

class Instructor(models.Model):
    id_instructor = models.IntegerField(primary_key=True)
    sueldo = models.IntegerField()
    rut_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_instructor)

    class Meta:
        db_table = 'db_instructor'

class Administrador(models.Model):
    id_administrador = models.IntegerField(primary_key=True)
    rut_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_administrador)

    class Meta:
        db_table = 'db_administrador'

class Taller(models.Model):
    id_taller = models.IntegerField(primary_key=True)
    nombre_taller = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_taller

    class Meta:
        db_table = 'db_taller'

class Salas:
    id_sala = models.CharField(primary_key=True, max_length=10)
    tamano = models.IntegerField()
    capacidad_max = models.IntegerField()

    def __str__(self):
        return self.id_sala

    class Meta:
        db_table = 'db_salas'

class Curso(models.Model):
    id_curso = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    descripcion = models.TextField(max_length=500)
    capacidad_max = models.IntegerField()
    imagen = models.ImageField()
    sala = models.ForeignKey(Salas, on_delete=models.CASCADE)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_curso)
    
    class Meta:
        db_table = 'db_curso'

class Materiales(models.Model):
    id_material = models.IntegerField(primary_key=True)
    nombre_material = models.CharField(max_length=55)
    cantidad = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_material)
    
    class Meta:
        db_table = 'db_materiales'

class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=10)

class Postulacion(models.Model):
    id_postulacion = models.IntegerField(primary_key=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    correo = models.CharField(max_length=20)
    numero = models.IntegerField()
    documentos = models.FileField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_postulacion)

    class Meta:
        db_table = 'db_postulacion'

class Inscripcion(models.Model):
    id_inscripcion = models.IntegerField(primary_key=True)
    fecha_inscripcion = models.DateField()
    hora_inscripcion = models.TimeField(auto_now_add=True)
    adulto_mayor = models.ForeignKey(AdultoMayor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_inscripcion)
    
    class Meta:
        db_table = 'db_inscripcion'

class Calificacion(models.Model):
    id_calificacion = models.IntegerField(primary_key=True)
    Calificacion = models.IntegerField()
    adulto_mayor = models.ForeignKey(AdultoMayor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_calificacion)

    class Meta:
        db_table = 'db_calificacion'

class CalifFinal(models.Model):
    id_calf_final = models.IntegerField(primary_key=True)
    calificacion_final = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_calf_final)

    class Meta:
        db_table = 'db_calf_final'

class Bonificacion(models.Model):
    id_bonificacion = models.IntegerField(primary_key=True)
    monto_bonificacion = models.IntegerField()
    calf_final = models.ForeignKey(CalifFinal, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_bonificacion)
    
    class Meta:
        db_table = 'db_bonificacion'

class Pago(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    monto_pago = models.IntegerField()
    fecha_pago = models.DateField(auto_now_add=True)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    bonificacion = models.ForeignKey(Bonificacion, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_pago)
    
    class Meta:
        db_table = 'db_pago'
