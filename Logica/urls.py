from django.urls import path
from .views import *

urlpatterns = [
    path('web-panel-admin/',WebPanelAdmin,name="webPanelAdmin"),
    path('', PageInicio,name="pagina_inicio"),
    path('especialidades', PageEspecialidades,name="pagina_especialidad"),
    path('doctores', PageDoctores,name="pagina_doctor"),
    path('contacto', PageContacto,name="pagina_contacto"),
    path('preguntas', PagePreguntas,name="pagina_pregunta"),
    path('consejos', PageConsejos,name="pagina_consejo"),
    path("consejo/<int:id>/",PageConsejoDetalle,name="PageConsejoDetalle"),
    path('nosotros', PageNosotros,name="pagina_nosotros"),
    
    
] 