from django.http.response import HttpResponse
from django.shortcuts import render
from AppGimnasio.models import musculacion, yoga, natacion
from AppGimnasio.forms import Musculacionformulario

# Create your views here.
def inicio(request):
   return render(request,'AppGimnasio/inicio.html')

def musculacion(request):
    return render(request, 'AppGimnasio/musculacion.html')

def yoga(request):
    return render(request,'AppGimnasio/yoga.html')    

def natacion(request):
    return render(request,'AppGimnasio/natacion.html')    
    
def musculacionformulario(request):
    if request.method == "POST":
        miFormulario = Musculacionformulario(request.POST)  
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data  
            musculacioninsta = musculacion( 
            nombre = informacion ['nombre'],
            apellido = informacion ['apellido'],
            fecha_ingreso = informacion ['fecha_ingreso']
            )
            musculacioninsta.save()
            return render(request, 'AppGimnasio/inicio.html')
    else: 
        miFormulario = Musculacionformulario()
        return render(request, 'AppGimnasio/musculacionformulario.html', {'miFormulario':miFormulario})

    