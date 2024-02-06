from django.shortcuts import render,redirect
from .models import *
from .info import INFORMACION_ALERGIKIDS
from django.db.models import Q

# Create your views here.
def PageInicio(request):
    navegacion = Navegaciones.objects.all()
    context = {
        "navegacion":navegacion,
        "info":INFORMACION_ALERGIKIDS
    }
    return render(request,'PageInicio.html',context)

def PageEspecialidades(request):
    # muestra solo las primeras 6 especialidades
    esp = Especialidades.objects.all()[:6]
    # muestra todas las especialidades
    # esp = Especialidades.objects.all()
    context={ 
        "especialidades":esp
    }
    return render(request,'pagina_especialidad.html',context)

def PageEspecialidadDetalle(request,id):
    esp = Especialidades.objects.get(id=id)
    ctx={
        "consejo":esp,
    }
    return render(request,'pagina_especialidad_detalle.html',ctx)

def PageDoctores(request):
    dr = Doctores.objects.all()
    context={
        "doctores":dr,
    }
    return render(request,'pagina_doctor.html',context)

def PageContacto(request):
    return render(request,'pagina_contacto.html')

def PagePreguntas(request):
    if request.method == 'POST':
        query = request.POST['query']
        objs = Preguntas.objects.filter(
            Q(pregunta__contains=query)|
            Q(respuesta__contains=query)|
            Q(fecha__contains=query))
        
    else:
        objs = Preguntas.objects.all()
        
    context={
        "preguntas":objs,
    }
    return render(request,'pagina_pregunta.html',context)

def PageConsejos(request):
    if request.method == 'POST':
        query = request.POST['query']
        consejos = consejos = Consejos.objects.filter(
            Q(titulo__contains=query)|
            Q(descripcion__contains=query)|
            Q(fecha__contains=query))     
    else:
        consejos = Consejos.objects.all()
    
    ctx={"consejo":consejos}
    
    return render(request,'pagina_consejo.html',ctx)

def PageConsejoDetalle(request,id):
    consejo = Consejos.objects.get(id=id)
    ctx={
        "consejo":consejo,
    }
    return render(request,'pagina_consejo_detalle.html',ctx)


def PageNosotros(request):
    return render(request,'pagina_nosotros.html')


def WebPanelAdmin(request):
    return render(request,'webPanelAdmin.html')
