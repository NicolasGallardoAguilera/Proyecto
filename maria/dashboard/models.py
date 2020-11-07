from django.db import models
# Create your models here.

class usuario(models.Model):
    nombre_usuario=models.CharField(primary_key=True,max_length=40)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    es_profesor=models.BooleanField()
    def __str__(self):
        return self.nombre_usuario

class curso(models.Model):
    codigo=models.CharField(primary_key=True,max_length=15)
    enseñanza=models.CharField(max_length=15)
    grado=models.CharField(max_length=30)
    letra=models.CharField(max_length=15)
    profesor_jefe=models.ForeignKey(usuario,on_delete=models.PROTECT)
    def __str__(self):
        return self.codigo


class alumno(models.Model):
    id_alumno=models.CharField(primary_key=True,max_length=40)
    año_cursado=models.CharField(max_length=30)
    asistencia=models.IntegerField()
    comuna=models.CharField(max_length=30)
    edad=models.CharField(max_length=30)
    enseñanza=models.CharField(max_length=30)
    grado=models.CharField(max_length=30)
    letra_curso=models.CharField(max_length=30)
    promedio_general=models.FloatField()
    rbd=models.CharField(max_length=30)
    sexo=models.CharField(max_length=30)
    id_curso=models.ForeignKey(curso,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.id_alumno