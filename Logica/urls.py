from django.urls import path
from .views import *

urlpatterns = [
    path('', PageInicio,name="pagina_inicio"),
    path('especialidades', PageEspecialidades,name="pagina_especialidad"),
    path('doctores', PageDoctores,name="pagina_doctor"),
    path('contacto', PageContacto,name="pagina_contacto"),
    path('preguntas', PagePreguntas,name="pagina_pregunta"),
    path('consejos', PageConsejos,name="pagina_consejo"),
    path('nosotros', PageNosotros,name="pagina_nosotros"),
] 