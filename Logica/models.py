from django.db import models
from .info import RUTAS_INICIO

# Create your models here.


class Especialidades(models.Model):
    nombre = models.CharField(max_length=50 ,null=False , verbose_name="Nomnbre de la Especialidad")
    descripcion = models.CharField(max_length=5000,null=False,verbose_name="Descripcion de la Especialidad")
    img = models.ImageField(blank=True,null=True ,upload_to="img_especialidades/")

    def __str__(self):
        return self.nombre 

class Doctores(models.Model):
    nombre = models.CharField(max_length=50 ,null=False , verbose_name="Nomnbre del Docotor")
    alias = models.CharField(max_length=15 ,null=False , verbose_name="Alias del Docotor")
    descripcion = models.CharField(max_length=5000,null=False,verbose_name="Descripcion del Doctor")
    telefono = models.IntegerField(null=True)
    whatsapp = models.IntegerField(null=True)
    correo = models.EmailField(max_length=220)
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    img = models.ImageField(blank=True,null=True ,upload_to="img_doctores/")

    def __str__(self):
        return self.nombre

class Servicios(models.Model):
    nombre = models.CharField(max_length=50 ,null=False , verbose_name="Nomnbre del Servicio")
    descripcion = models.CharField(max_length=5000,null=False,verbose_name="Descripcion del Servicio")
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    img = models.ImageField(blank=True,null=True ,upload_to="img_servicios/")

class Preguntas(models.Model):
    pregunta = models.CharField(max_length=500 ,null=False , verbose_name="Pregunta")
    respuesta = models.CharField(max_length=500 ,null=False , verbose_name="Respuesta")
    fecha = models.DateField(auto_created=True)
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.pregunta

class Consejos(models.Model):
    titulo = models.CharField(max_length=100 ,null=False , verbose_name="Titulo")
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.TextField(verbose_name="Descripcion")
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    img = models.ImageField(blank=True,null=True ,upload_to="img_consejos/")

    def __str__(self):
        return f"{self.titulo} {self.especialidad}"
    

class Navegaciones(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    link = models.CharField(choices=RUTAS_INICIO,max_length=200)
    img = models.ImageField(upload_to="img_inicio/")

    def __str__(self):
        return self.titulo








