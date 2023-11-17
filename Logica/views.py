from django.shortcuts import render
from .models import *
from .info import INFORMACION_ALERGIKIDS

# Create your views here.
def PageInicio(request):
    navegacion = Navegaciones.objects.all()
    context = {
        "navegacion":navegacion,
        "info":INFORMACION_ALERGIKIDS
    }
    return render(request,'PageInicio.html',context)

def PageEspecialidades(request):
    esp = Especialidades.objects.all()
    context={ 
        "especialidades":esp
    }
    return render(request,'pagina_especialidad.html',context)

def PageDoctores(request):
    dr = Doctores.objects.all()
    context={
        "doctores":dr,
    }
    return render(request,'pagina_doctor.html',context)

def PageContacto(request):
    return render(request,'pagina_contacto.html')

def PagePreguntas(request):
    pr = Preguntas.objects.all()
    context={
        "preguntas":pr[:2],
    }
    return render(request,'pagina_pregunta.html',context)

def PageConsejos(request):
    return render(request,'pagina_consejo.html')

def PageNosotros(request):
    return render(request,'pagina_nosotros.html')


def WebPanelAdmin(request):
    return render(request,'webPanelAdmin.html')
