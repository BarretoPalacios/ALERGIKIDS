from django.contrib import admin
from .models import *


# Register your models here.
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion','img')

admin.site.register(Especialidades, EspecialidadAdmin)

class DoctoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'alias','telefono','especialidad')

admin.site.register(Doctores, DoctoresAdmin)
admin.site.register(Servicios)
admin.site.register(Preguntas)
admin.site.register(Consejos)
admin.site.register(Navegaciones)